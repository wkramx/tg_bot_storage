import telebot
from telebot import types

f = open("API_TOKEN.txt", "r").readline()
API_TOKEN = f

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Hi there, I am TelegramStorageBot ")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    goods = types.KeyboardButton("👟 Goods")
    deliveries = types.KeyboardButton("📦 Deliveries")
    calculator = types.KeyboardButton("➕ Calculator")
    addresses = types.KeyboardButton("🏠 Addresses and recipients")
    profile = types.KeyboardButton("👤 Profile")
    help_faq = types.KeyboardButton("❔ Help")
    markup.add(goods, deliveries, calculator, addresses, profile, help_faq)
    bot.send_message(message.chat.id, "Choose option", reply_markup=markup)



bot.infinity_polling()