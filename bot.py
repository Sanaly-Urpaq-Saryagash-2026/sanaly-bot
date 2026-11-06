import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN", "9009796462:AAEF67FCci1JSFJRsuDbzkiGq6lu7PQv6-o")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Сәлем! Sanaly Urpaq Saryagash бот іске қосылды! 🌸")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"Сіз жаздыңыз: {message.text}")

print("Bot started...")
bot.infinity_polling()
