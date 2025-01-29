import os
import base64
from datetime import datetime, timezone
from PIL import Image
from telegram import Update
from telegram.ext import CallbackContext
from utils import generate_description
from database.mongo import Mongo

# Initialize MongoDB connection and collection
mongo = Mongo()
file_collection = mongo.get_collection('files')

async def file_analysis(update: Update, context: CallbackContext):
    """Analyze the file sent by the user."""
    user_message = update.message
    chat_id = user_message.chat_id
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d_%H-%M-%S')

    # Ensure the downloads directory exists
    download_dir = 'downloads'
    os.makedirs(download_dir, exist_ok=True)

    if user_message.document:
        await handle_document(user_message, chat_id, timestamp, download_dir, context)
    elif user_message.photo:
        await handle_photo(user_message, chat_id, timestamp, download_dir, context)

async def handle_document(user_message, chat_id, timestamp, download_dir, context):
    """Handle document files sent by the user."""
    file_id = user_message.document.file_id
    file_name = user_message.document.file_name
    file_size = user_message.document.file_size
    file_path = os.path.join(download_dir, file_name)

    file = await context.bot.get_file(file_id)
    await file.download_to_drive(file_path)

    try:
        description = generate_description_from_file(file_path)
        bot_response = f"Description of the file '{file_name}' is: {description}"

        file_metadata = {
            'chat_id': chat_id,
            'file_name': file_name,
            'file_size': file_size,
            'description': description,
            'timestamp': timestamp
        }
        file_collection.insert_one(file_metadata)
    except Exception as err:
        print(f'An unexpected error occurred: {err}')
        bot_response = 'An unexpected error occurred. Please try again later.'

    await user_message.reply_text(bot_response)

async def handle_photo(user_message, chat_id, timestamp, download_dir, context):
    """Handle photo files sent by the user."""
    photo = user_message.photo[-1]
    file_id = photo.file_id
    file_path = os.path.join(download_dir, f"photo_{chat_id}_{timestamp}.jpg")

    file = await context.bot.get_file(file_id)
    await file.download_to_drive(file_path)

    try:
        description = generate_description_from_image(file_path)
        bot_response = f"Description of the photo is: {description}"

        image_metadata = {
            'chat_id': chat_id,
            'file_name': 'photo',
            'file_size': 0,
            'description': description,
            'timestamp': timestamp
        }
        file_collection.insert_one(image_metadata)
    except Exception as err:
        print(f'An unexpected error occurred: {err}')
        bot_response = 'An unexpected error occurred. Please try again later.'

    await user_message.reply_text(bot_response)

def generate_description_from_file(file_path):
    """Generate a description for a document file."""
    try:
        with open(file_path, 'rb') as file:
            data = base64.b64encode(file.read()).decode('utf-8')
        prompt = "Generate a description for the document."
        context = [prompt, {'mime_type': 'application/pdf', 'data': data}]
        return generate_description(context)
    except Exception as e:
        print(f"Error generating description from file: {e}")
        return "Unable to generate description."

def generate_description_from_image(image_path):
    """Generate a description for an image file."""
    try:
        with Image.open(image_path) as img:
            img_data = base64.b64encode(img.tobytes()).decode('utf-8')
        prompt = "Generate a description for the image."
        context = [img_data, prompt]
        return generate_description(context)
    except Exception as e:
        print(f"Error generating description from image: {e}")
        return "Unable to generate description."
