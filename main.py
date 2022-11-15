import telebot

bot = telebot.TeleBot('5659318525:AAECVjS61OpZTt9LXOV02hzi6jujdvI-4y0', parse_mode=None) # You can pythonset parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def start(messege):
    mess = f'Привет,{messege.from_user.first_name} {messege.from_user.last_name}. Я бот созданный Луневским Иваном. я пока ничего не умею но это скоро изменится!'
    bot.send_message(messege.chat.id,mess,parse_mode='html')

bot.polling(none_stop=True)