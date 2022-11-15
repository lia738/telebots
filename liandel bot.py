import telebot

bot = telebot.TeleBot('5659318525:AAECVjS61OpZTt9LXOV02hzi6jujdvI-4y0', parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def start(messege):
    bot.send_message(messege.chat.id,'Привет,я бот созданный Луневским Иваном. Я пока ничего не умею, но это скоро изменится')

bot.polling(none_stop=True)
