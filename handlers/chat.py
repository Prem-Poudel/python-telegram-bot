from telegram import Update
from telegram.ext import CallbackContext
import google.generativeai as genai
from database.mongo import Mongo
from dotenv import load_dotenv
import os
from datetime import datetime, timezone
import emoji
from features import sentiment_analysis as sa

load_dotenv()

TOKEN = os.getenv('GEMINI_TOKEN')
genai.configure(api_key=TOKEN)

# initialize the Mongo class
mongo = Mongo()
chat_collection = mongo.get_collection('chats')

async def gemini_chat(update: Update, context: CallbackContext):
    '''Chat with the Gemini chatbot'''
    user_message = update.message.text
    chat_id = update.message.chat_id
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

    try:
        model = genai.GenerativeModel(model_name='gemini-1.5-flash')
        response = model.generate_content(user_message)

        if response and hasattr(response, 'text'):
            bot_response = response.text
            bot_response = sa.add_emoji_based_on_sentiment(bot_response)
            await update.message.reply_text(bot_response)
        else:
            bot_response = 'I am sorry, I could not understand your message. ' + emoji.emojize(':confused:', language='alias')
            await update.message.reply_text()

        chat_entry = {
            'chat_id': chat_id,
            'user_message': user_message,
            'bot_response': bot_response,
            'timestamp': timestamp
        }

        chat_collection.insert_one(chat_entry)

    except Exception as err:
        print(f'An unexpected error occured: {err}')

        await update.message.reply_text('An unexpected error occured. Please try again later. ' + emoji.emojize(':disappointed:', language='alias'))
