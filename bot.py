from telegram.ext import Application, MessageHandler, filters, CommandHandler
from handlers.file_analysis import file_analysis
from handlers.registration import start, contact
from handlers.chat import gemini_chat


import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.CONTACT,  contact))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, gemini_chat))
    application.add_handler(MessageHandler(filters.PHOTO, file_analysis))
    application.add_handler(MessageHandler(filters.Document.ALL, file_analysis))


    application.run_polling()



if __name__ == '__main__':
    main()