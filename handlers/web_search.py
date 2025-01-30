from telegram import Update
from telegram.ext import CallbackContext
from database.mongo import Mongo
from utils import generate_description
from datetime import datetime, timezone
import google.generativeai as genai
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

# Google Search API Key
API_KEY = os.getenv('GOOGLE_SEARCH_TOKEN')

# Google Search Engine ID
SEARCH_ENGINE_ID = os.getenv('GOOGLE_SEARCH_ENGINE_ID')


mongo = Mongo()
websearch_collection = mongo.get_collection('websearches')

def google_search(query):
    '''Fetch search results from Google Search API.'''
    try:
        service = build("customsearch", "v1", developerKey=API_KEY)
        res = service.cse().list(q=query, cx=SEARCH_ENGINE_ID).execute()
        results = res.get('items', [])

        return [f"- [{item['title']}]({item['link']})" for item in results] if results else []
    except Exception as e:
        print(f'Error fetching search results: {e}')
        return []


async def websearch(update: Update, context: CallbackContext):
    '''
    Search the web for the user's query.
    It will search the web using the user's query and return the summary of the search results including the top urls.
    '''
    query = ' '.join(context.args)
    if not query:
        await update.message.reply_text('Please provide a query to search.')
        return
    
    search_results = google_search(query)
    if not search_results:
        await update.message.reply_text('No search results found.')
        return
    
    prompt=f"Summarize the search results for the query: {query}".join(search_results)
    
    response = generate_description(prompt)


    if response:
        await update.message.reply_text(f'**Search Results for:** {query}\n\n{response}\n\n**Resources**\n\n{search_results[:5]}')
    else:
        await update.message.reply_text('An error occurred while searching the web.')
    
    websearch_metadata = {
        'chat_id': update.message.chat_id,
        'query': query,
        'response': response,
        'timestamp': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    }
    websearch_collection.insert_one(websearch_metadata)


    
    

