from telegram import Update
from telegram.ext import CallbackContext
from database.mongo import Mongo
from utils import generate_description
from datetime import datetime, timezone
import emoji
from features import sentiment_analysis as sa


# initialize the Mongo class
mongo = Mongo()
chat_collection = mongo.get_collection('chats')

async def gemini_chat(update: Update, context: CallbackContext):
    '''Chat with the Gemini chatbot'''
    user_message = update.message.text
    chat_id = update.message.chat_id
    timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

    try:
        bot_response = generate_description(user_message)
        bot_response = sa.add_emoji_based_on_sentiment(bot_response)
    

        chat_entry = {
            'chat_id': chat_id,
            'user_message': user_message,
            'bot_response': bot_response,
            'timestamp': timestamp
        }

        chat_collection.insert_one(chat_entry)
        await update.message.reply_text(bot_response)

    except Exception as err:
        print(f'An unexpected error occured: {err}')

        await update.message.reply_text('An unexpected error occured. Please try again later. ' + emoji.emojize(':disappointed:', language='alias'))
