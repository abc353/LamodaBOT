import telebot
import constants
from telebot import types
bot = telebot.TeleBot(constants.token)
main_menu = types.ReplyKeyboardMarkup(False, True, False)
main_menu.row('Контактная информация')
main_menu.row('Правила работы с отменами и переносами')
otmena = types.ReplyKeyboardMarkup(False)
otmena.row('Как мне работать с отменами и переносами?')
otmena.row('Когда можно отменить заказ?')
otmena.row('Главное меню')
@bot.message_handler(commands=('start'))
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать с Ламода БОТ', reply_markup=main_menu)
@bot.message_handler(content_types=('text'))
def handle_text(message):
    if message.text == "Контактная информация":
        bot.send_message(message.chat.id, "Кол Центр +74995004959\nДежурный СВ+79160558030\nДежурный механик +79150110787\nДежурный кассир +79175805523\nПаркоматика  88003015748\nМокка 88007077236\niboxPro +74955055045 88003334526\nСБ +79999991489")
    elif message.text == "Правила работы с отменами и переносами":
        bot.send_message(message.chat.id, "Правила работы с отменами и переносами", reply_markup=otmena)
    elif message.text == "Как мне работать с отменами и переносами?":
        bot.send_message(message.chat.id, "1 - Выясняем причину\n2 - Предлагаем доставку заказа в другой интервал сегодня же\n3 - Предлагаем доставку по другому адресу, главное чтобы клиент принял сегодня. Адрес согласовываем с супервайзером")
    elif message.text == "Когда можно отменить заказ?":
        bot.send_message(message.chat.id, "1 - Отмена по просьбе клиента (крайне желательно подтверждение отмены по рабочему телефону в звонке\n2 - У заказа кончаются попытки доставки max3( смотрим через статус недозвон или в маршрутнике\n2.1 - У заказа кончаются дни хранения на складе max5\n3 - Фактический адрес доставки не входит в зону Южного склада ( уточняем у супервайзера). Только оформление нового заказа с корректным адресом. Перенос невозможен")
    elif message.text == "Главное меню":
        bot.send_message(message.chat.id, "Главное меню", reply_markup=main_menu)
    else: bot.send_message(message.chat.id, "я тебя не понимаю")
bot.polling()