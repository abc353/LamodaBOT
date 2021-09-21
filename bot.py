import telebot
import constants
from telebot import types
bot = telebot.TeleBot(constants.token)
main_menu = types.ReplyKeyboardMarkup(False, True, False)
main_menu.row('Заказ,Оплата,Опоздания,Нет соединения')
main_menu.row('Где бумажный чек?')
main_menu.row('Контактная информация', 'Где мой промокод')
menu_pravila = types.ReplyKeyboardMarkup(False)
menu_pravila.row('Как мне работать с отменами и переносами?')
menu_pravila.row('Когда отменять заказ?', 'Не успеваю в интервал')
menu_pravila.row('Заказ остался на карте', 'Не прошла оплата')
menu_pravila.row('Нет соединения, Anyconnect', 'Планшет не включается')
menu_pravila.row('Главное меню')
menu_stop = types.ReplyKeyboardRemove()


@bot.message_handler(commands='start')
def welcome(message):
    if message.chat.type == 'private':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIIQGFJQJ6aR-pSJuHPw2evH6cJJTOOAAJFAAN4qOYPxT4UDl0DPssgBA', reply_markup=main_menu)


@bot.message_handler(commands='gohome')
def handle_text(message):
    bot.send_location(message.chat.id, 55.728270423944274, 37.7148733308119)


@bot.message_handler(content_types='text')
def handle_text(message):
    if message.chat.type == 'private':
        if message.text == "Контактная информация":
            bot.send_message(message.chat.id, constants.contact, parse_mode="Markdown", reply_markup=menu_stop)
        elif message.text == "Где мой промокод":
            bot.send_message(message.chat.id, constants.promokod, parse_mode="Markdown", reply_markup=menu_stop)
        elif message.text == "Где бумажный чек?":
            bot.send_message(message.chat.id, constants.elchek, parse_mode="Markdown", reply_markup=menu_stop)
        elif message.text == "Заказ,Оплата,Опоздания,Нет соединения":
            bot.send_message(message.chat.id, "Соблюдай правила", reply_markup=menu_pravila)
        elif message.text == "Как мне работать с отменами и переносами?":
            bot.send_message(message.chat.id, constants.perenos, parse_mode="Markdown")
        elif message.text == "Когда отменять заказ?":
            bot.send_message(message.chat.id, constants.otmena, parse_mode="Markdown")
        elif message.text == "Не успеваю в интервал":
            bot.send_message(message.chat.id, constants.opozdanie, parse_mode="Markdown")
        elif message.text == "Заказ остался на карте":
            bot.send_message(message.chat.id, constants.bezcheka, parse_mode="Markdown")
        elif message.text == "Не прошла оплата":
            bot.send_message(message.chat.id, constants.oplata, parse_mode="Markdown")
        elif message.text == "Планшет не включается":
            bot.send_message(message.chat.id, """Вынимаешь АКБ, вставляешь кабель питания. `он должен заряжать`
Вставляешь АКБ, появляется молния, потом начинают бежать проценты зеленым - перетыкаешь АКБ именно в этот момент.
Планшет включается""", parse_mode="Markdown")
        elif message.text == "Нет соединения, Anyconnect":
            bot.send_animation(message.chat.id, animation=constants.vpn)
            bot.send_message(message.chat.id, "Добавляем сертификат как на видео")
        elif message.text == "Главное меню":
            bot.send_message(message.chat.id, "Главное меню", reply_markup=main_menu)
        elif "перен" in message.text.lower():
            bot.send_message(message.chat.id, constants.perenos, parse_mode="Markdown")
        elif "отмен" in message.text.lower():
            bot.send_message(message.chat.id, constants.otmena, parse_mode="Markdown")
#        elif "работает" and "айбокс" in message.text.lower():
#            bot.reply_to(message.chat.id, "*Позвони в службу поддержки iBox +78003334526*", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "пиши /start")
 #   elif message.chat.type == 'group':
  #      if "работает" and "айбокс" in message.text.lower():
  #        bot.reply_to(message.chat.id, "*Позвони в службу поддержки iBox +78003334526*", parse_mode="Markdown")


bot.polling()
