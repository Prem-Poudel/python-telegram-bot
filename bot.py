from telegram.ext import Application, MessageHandler, filters, CommandHandler
from handlers.registration import start, contact


import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.CONTACT,  contact))

    application.run_polling()



if __name__ == '__main__':
    main()