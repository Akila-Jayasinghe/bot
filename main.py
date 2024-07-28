import os
import telebot

bot = telebot.TeleBot("API Key Here")

@bot.message_handler(commands=["Start"])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm Akila's chat bot.")

@bot.message_handler(commands=["How"])
def send_message(message):
    bot.send_message(message, "https://youtube.com")

bot.polling()
