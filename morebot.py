from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler, CallbackQueryHandler)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import logging
import pymysql as SQL
import sys
import time
from pprint import pprint
import random
import datetime
import json
import requests

updater = Updater(token='1114317585:AAG0xZjJxijkfRMaPSQHhM2mJqD8zcoqjsI', use_context=True)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

print(logger.name)

USER_CRED, COMMENT, SECTORS, SECTOR_COMP, PHOTO, LOCATION, GET_BIN_ID = range(7)


def start(bot, update):
    global username

    try:

        username = update.message.from_user

        keyboard = [[InlineKeyboardButton("Feeling Today", callback_data='report')],
                    [InlineKeyboardButton("Temparature", callback_data='compliment')]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Howdy! I am your helpful health assistant.'
                                'Send /cancel to stop session.\n\n'
                                ' Please choose:', reply_markup=reply_markup)
    except Exception as ex:
        print("Exception Caught: " + str(ex))
    return USER_CRED


def user_cred(bot, update):
    query = update.callback_query

    if query.data == 'report':
        bot.edit_message_text(text="Use /comment to report an incident",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
        return COMMENT

    elif query.data == 'query_bin':
        bot.edit_message_text(text="Use /id to read off your bin number",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
        return GET_BIN_ID

    elif query.data == 'compliment':
        bot.edit_message_text(text="Thanks for choosing this option. Use /sectors to navigate different sectors",
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
        return SECTORS

    elif query.data == 'worker':
        bot.edit_message_text(text="Confirm your password.",
                         chat_id=query.message.chat_id,
                         message_id=query.message.message_id)


def done(bot, update):
    update.message.reply_text('Thank you! :) .')
    return ConversationHandler.END


def comment(bot, update):
    update.message.reply_text('How do you feel?')
    return PHOTO


def cancel(bot, update):
    update.message.reply_text('Bye! You cancelled the session', reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    dp = updater.dispatcher
    conv_handler = ConversationHandler(entry_points=[CommandHandler('start', start)], states={
            USER_CRED: [CallbackQueryHandler(user_cred)],
            COMMENT: [CommandHandler('comment', comment)]},
            fallbacks=[CommandHandler('cancel', cancel)])

    dp.add_handler(conv_handler)

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()