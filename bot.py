import telebot
TOKEN = "9103569711:AAGTtahQK_7-a3dUReUZSHXDiKKS-BsVQA8"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salem! Bot ozhyl na Render! ❤️")

@bot.message_handler(func=lambda m: True)
def all_msg(message):
    bot.send_message(message.chat.id, f"Siz jazdynyz: {message.text}")

print("Bot gotov k rabote...")
bot.infinity_polling()
