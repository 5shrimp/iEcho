# -*- coding: utf-8 -*-
import config
import telebot


# Я назову его iEcho_bot
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def send_message_back(message): 
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
