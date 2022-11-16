import telebot
import random
bot = telebot.TeleBot('5659318525:AAECVjS61OpZTt9LXOV02hzi6jujdvI-4y0', parse_mode=None) # You can pythonset parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def start(messege):
    mess = f'Привет, {messege.from_user.first_name} {messege.from_user.last_name}. Я бот созданный Луневским Иваном. я пока ничего не умею но это скоро изменится!'
    bot.send_message(messege.chat.id,mess,parse_mode='html')
    bot.send_message(messege.chat.id, 'теперь я умею кидать кубик, просто напиши /dice или /dice_sticker', parse_mode='html')

@bot.message_handler(commands=['dice'])
def dice(messege):
    kube = random.randint(1,6)
    mess =f'выпало значение {kube}'
    bot.send_message(messege.chat.id, 'Бросаем куб....', parse_mode='html')
    bot.send_message(messege.chat.id,mess,parse_mode='html')

@bot.message_handler(commands=['dice_sticker'])
def dice_sticker(messege):
    bot.send_message(messege.chat.id, 'Бросаем куб....', parse_mode='html')
    bot.send_dice(messege.chat.id)

@bot.message_handler()
def messege_from_user(messege):
    what=open('what.jpg','rb')
    bot.send_photo(messege.chat.id, what)

bot.polling(none_stop=True)