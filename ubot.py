import telebot

bot = telebot.TeleBot('5748923218:AAHeeMpLQ2KZf_H7Fg-RZrcIEYmavmxsbDo')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


bot.polling(none_stop=True)