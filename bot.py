import telebot
import constants
from telebot import types
bot = telebot.TeleBot(constants.token)
main_menu = types.ReplyKeyboardMarkup(False, True, False)
main_menu.row('Соблюдай правила')
main_menu.row('Где бумажный чек?')
main_menu.row('Контактная информация', 'Где мой промокод')
menu_pravila = types.ReplyKeyboardMarkup(False)
menu_pravila.row('Как мне работать с отменами и переносами?')
menu_pravila.row('Когда отменять заказ?', 'Я не успеваю в интервал?')
menu_pravila.row('Заказ остался на карте', 'Проверяем оплату')
menu_pravila.row('AnyConnect не работает, нет соединения')
menu_pravila.row('Главное меню')
menu_stop = types.ReplyKeyboardRemove()
@bot.message_handler(commands='start')
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать с Ламода БОТ', reply_markup=main_menu)
@bot.message_handler(commands='gohome')
def handle_text(message):
    bot.send_location(message.chat.id, 55.728270423944274, 37.7148733308119)

@bot.message_handler(content_types='text')
def handle_text(message):
    if message.text == "Контактная информация":
        bot.send_message(message.chat.id, constants.contact, parse_mode="Markdown", reply_markup=menu_stop)
    elif message.text == "Где мой промокод":
        bot.send_message(message.chat.id, constants.promokod, parse_mode="Markdown", reply_markup=menu_stop)
    elif message.text == "Где бумажный чек?":
        bot.send_message(message.chat.id, constants.elchek, parse_mode="Markdown", reply_markup=menu_stop)
    elif message.text == "Соблюдай правила":
        bot.send_message(message.chat.id, "Соблюдай правила", reply_markup=menu_pravila)
    elif message.text == "Как мне работать с отменами и переносами?":
            bot.send_message(message.chat.id, constants.perenos, parse_mode="Markdown")
    elif message.text == "Когда отменять заказ?":
            bot.send_message(message.chat.id, constants.otmena, parse_mode="Markdown")
    elif message.text == "Я не успеваю в интервал?":
            bot.send_message(message.chat.id, constants.opozdanie, parse_mode="Markdown")
    elif message.text == "Заказ остался на карте":
            bot.send_message(message.chat.id, constants.bezcheka, parse_mode="Markdown")
    elif message.text == "Проверяем оплату":
            bot.send_message(message.chat.id, constants.oplata, parse_mode="Markdown")
   # elif message.text == "AnyConnect не работает, нет соединения":
    #        bot.send_video(message.chat.id, video)
    elif message.text == "Главное меню":
            bot.send_message(message.chat.id, "Главное меню", reply_markup=main_menu)
    else: bot.send_message(message.chat.id, "пиши /start")

@bot.message_handler(content_types='video')
def handle_docs_video(message):
    id = message.document.file_id
    info = bot.get_file(id)
    bot.send_message(message.chat.id, 'super')
    print(message.id)
bot.polling()
