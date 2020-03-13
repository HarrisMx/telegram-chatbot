import telebot
from telebot import types
import time
from database import MoreBot_DB

bot = telebot.TeleBot("1114317585:AAG0xZjJxijkfRMaPSQHhM2mJqD8zcoqjsI")
chat_id = ''

bot_db = MoreBot_DB()

bot_db.conenct()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    try:
        chat_id = message.chat.id

        markup = types.ReplyKeyboardMarkup(row_width=1)
        bot_db.setName(message.from_user.first_name)
        bot_db.setSurname(message.from_user.last_name)
        itembtn1 = types.KeyboardButton('Feeling?')
        itembtn2 = types.KeyboardButton('Temperature')
        markup.add(itembtn1, itembtn2)
        bot.send_message(chat_id, "Hi " + bot_db.getUser() + ", Please choose an option to tell us how you are feeling: ", reply_markup=markup)
    except Exception as exc:
        print("Error : ", exc)


@bot.message_handler(commands=['exit'])
def exit_bot(message):
    bot.reply_to(message, "Are you sure you are done?")


@bot.message_handler(func=lambda message: message.text == 'Feeling?' and message.content_type == 'text')
def mood_handler(message):
    chat_id = message.chat.id
    all_lang_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    all_lang_markup.add(u'\U0001F603', u'\U0001F61E', u'\U0001F629')
    bot.send_message(chat_id, "How are you feeling: ", reply_markup=all_lang_markup)


@bot.message_handler(func=lambda message: message.text == 'Temperature' and message.content_type == 'text')
def template_handler(message):
    chat_id = message.chat.id
    bot.reply_to(message, "I got your Temperature reply")


@bot.message_handler(func=lambda message: message.text == u'\U0001F603')
def happy(message):
    chat_id = message.chat.id
    bot.reply_to(message, "Glad you are having a great day please shout if I can help with anything")
    bot_db.new_record('Happy', message.chat.id)
    hideBoard = types.ReplyKeyboardRemove(selective=False)
    bot.reply_to(message, 'Thank you for your response, bye for now.', reply_markup=hideBoard)


@bot.message_handler(func=lambda message: message.text == u'\U0001F61E')
def sad(message):
    chat_id = message.chat.id
    bot.reply_to(message, "Hope your day goes better, please let me know if I can help you")
    bot_db.new_record('Sad', message.chat.id)
    hideBoard = types.ReplyKeyboardRemove(selective=False)
    bot.reply_to(message, 'Thank you for your response, bye for now.', reply_markup=hideBoard)


@bot.message_handler(func=lambda message: message.text == u'\U0001F629')
def sick(message):
    chat_id = message.chat.id
    bot.reply_to(message, "Ah shucks, please shout if I can help with anything.")
    bot_db.new_record('Not Well', message.chat.id)
    hideBoard = types.ReplyKeyboardRemove(selective=False)
    bot.reply_to(message, 'Thank you for your response, bye for now.', reply_markup=hideBoard)


bot.polling()