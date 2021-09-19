import telebot
import constants
from telebot import types
bot = telebot.TeleBot(constants.token)
main_menu = types.ReplyKeyboardMarkup(False, True, False)
main_menu.row('Контактная информация', 'Где мой промокод')
main_menu.row('Соблюдай правила')
menu_pravila = types.ReplyKeyboardMarkup(False)
menu_pravila.row('Как мне работать с отменами и переносами?')
menu_pravila.row('Когда можно отменить заказ?', 'Я не успеваю в интервал?')
menu_pravila.row()
menu_pravila.row('Главное меню')
menu_stop = types.ReplyKeyboardRemove()
@bot.message_handler(commands='start')
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать с Ламода БОТ', reply_markup=main_menu)
#@bot.message_handler(commands='gohome')
#def handle_text(message):
#    kuda = types.InlineKeyboardMarkup()
#    kuda_button = types.InlineKeyboardButton(text="Склад", callback_data="test")
#    kuda.add(kuda_button)
#    bot.send_message(message.chat.id, 'Построить маршрут:', reply_markup=kuda)

@bot.message_handler(content_types='text')
def handle_text(message):
    if message.text == "Контактная информация":
        bot.send_message(message.chat.id, constants.contact, parse_mode="Markdown", reply_markup=menu_stop)
    elif message.text == "Где мой промокод":
        bot.send_message(message.chat.id, constants.promokod, parse_mode="Markdown", reply_markup=menu_stop)
    elif message.text == "Соблюдай правила":
        bot.send_message(message.chat.id, "Соблюдай правила", reply_markup=menu_pravila)
    elif message.text == "Как мне работать с отменами и переносами?":
            bot.send_message(message.chat.id, constants.perenos, parse_mode="Markdown")
    elif message.text == "Когда можно отменить заказ?":
            bot.send_message(message.chat.id, constants.otmena, parse_mode="Markdown")
    elif message.text == "Я не успеваю в интервал?":
            bot.send_message(message.chat.id, constants.opozdanie, parse_mode="Markdown")
    elif message.text == "Главное меню":
            bot.send_message(message.chat.id, "Главное меню", reply_markup=main_menu)
    else: bot.send_message(message.chat.id, "пиши /start")


bot.polling()
