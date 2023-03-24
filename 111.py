import telebot
token='363684825:AAGjj4rdAoDZScibOTIczoe0Uu5QVDvHMWY'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_polling()