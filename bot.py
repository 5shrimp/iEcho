# -*- coding: utf-8 -*-
import config
import telebot

from telebot import types

# Я назову его iEcho_bot
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def send_message_back(message):
    # Эхо бота
    bot.send_message(message.chat.id, message.text)

    # Кастомная клава с вариантами
    markup = types.ReplyKeyboardMarkup()
    markup.row('🧀 сыр ', ' 🌭 хот-дог ' )
    markup.row(' 🌯 буррито ', ' 🍕 пицца ')
    markup.row(' 🌮 тако ' , ' 🍜 рамен' )
    markup.row(' 🍔 бургер ', ' 🍩 пончик ')
    bot.send_message(message.chat.id, " Что будешь заказывать? ", reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)
