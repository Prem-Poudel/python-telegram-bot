from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext
from database.mongo import Mongo

mongo = Mongo()

async def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    username = update.message.chat.username

    registration_status = mongo.register_user(first_name, username, chat_id)

    if registration_status == "Registration successful. Please provide your phone number.":
        keyboard = [[KeyboardButton("Share your Phone Number", request_contact=True)]]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        await update.message.reply_text(
            registration_status,
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(registration_status)

async def contact(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    phone_number = update.message.contact.phone_number

    phone_number_status = mongo.store_phone_number(chat_id, phone_number)

    await update.message.reply_text(phone_number_status)

