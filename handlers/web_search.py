from telegram import Update
from telegram.ext import CallbackContext
from database.mongo import Mongo
from utils import generate_description
from datetime import datetime, timezone
import google.generativeai as genai


mongo = Mongo()
websearch_collection = mongo.get_collection('websearches')



async def websearch(update: Update, context: CallbackContext):
    '''
    Search the web for the user's query.
    It will search the web using the user's query and return the summary of the search results including the top urls.
    '''
    query = ' '.join(context.args)
    if not query:
        await update.message.reply_text('Please provide a query to search.')
        return
    
    prompt=f"Perform a search for: {query}. Summarize the top results with relevant web links if possible."
    response = generate_description(prompt)


    if response:
        await update.message.reply_text(f'**Search Results for:** {query}\n\n{response}')
    else:
        await update.message.reply_text('An error occurred while searching the web.')
    
    websearch_metadata = {
        'chat_id': update.message.chat_id,
        'query': query,
        'response': response,
        'timestamp': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    }
    websearch_collection.insert_one(websearch_metadata)


    
    

