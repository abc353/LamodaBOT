import random

import telebot
import constants
from telebot import types
bot = telebot.TeleBot(constants.token)
main_menu = types.ReplyKeyboardMarkup(False, True, False)
main_menu.row('Заказ,Оплата,Опоздания,Нет соединения')
main_menu.row('Где бумажный чек?', 'Памятки')
main_menu.row('Контактная информация', 'Где мой промокод')
menu_pravila = types.ReplyKeyboardMarkup(False)
menu_pravila.row('Как мне работать с отменами и переносами?')
menu_pravila.row('Когда отменять заказ?', 'Не успеваю в интервал')
menu_pravila.row('Заказ остался на карте', 'Не прошла оплата')
menu_pravila.row('Нет соединения, Anyconnect', 'Планшет не включается')
menu_pravila.row('Главное меню')
menu_pamyatki = types.ReplyKeyboardMarkup(False)
menu_pamyatki.row('БПС', 'Удаленная касса')
menu_pamyatki.row('Подозрительный клиент')
menu_pamyatki.row('Главное меню')
menu_uk_but = types.InlineKeyboardButton("Далее", callback_data='dalee')
menu_uk = types.InlineKeyboardMarkup()
menu_uk.add(menu_uk_but)
menu_stop = types.ReplyKeyboardRemove()


@bot.message_handler(commands='start')
def welcome(message):
    if message.chat.type == 'private':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIIQGFJQJ6aR-pSJuHPw2evH6cJJTOOAAJFAAN4qOYPxT4UDl0DPssgBA', reply_markup=main_menu)


@bot.message_handler(commands='gohome')
def handle_text(message):
    bot.send_location(message.chat.id, 55.728270423944274, 37.7148733308119)

# ДЛЯ БОТА -------------------------------------------------------------------------------------------------------------
@bot.message_handler(content_types='text')
def handle_text(message):
    if message.chat.type == 'private':
        if message.text == "Контактная информация":
            bot.send_message(message.chat.id, constants.contact, parse_mode="Markdown", reply_markup=menu_stop)
        elif message.text == "Где мой промокод":
            bot.send_message(message.chat.id, constants.promokod, parse_mode="Markdown", reply_markup=menu_stop)
        elif message.text == "Где бумажный чек?":
            bot.send_message(message.chat.id, constants.elchek, parse_mode="Markdown", reply_markup=menu_stop)
        elif message.text == "Памятки":
            bot.send_message(message.chat.id, "Памятки", reply_markup=menu_pamyatki)
        elif message.text == "Заказ,Оплата,Опоздания,Нет соединения":
            bot.send_message(message.chat.id, "Соблюдай правила", reply_markup=menu_pravila)
        elif message.text == "Подозрительный клиент":
            bot.send_message(message.chat.id, constants.pk, parse_mode="Markdown")
        elif message.text == "БПС":
            bot.send_animation(message.chat.id, animation=constants.bps, parse_mode="Markdown")
            bot.send_message(message.chat.id, """Сверяем позицию на соответствие:
1 - Общий вид `достаем из прозрачного пакета`
2 - Цвет, оттенок
3 - Наличие пришитой бирки бренда
4 - Вещь чистая, не пахнет, не стираная
5 - Проверяем комплект `пояс, верх низ, капюшон, доп сумочка - смотрим фото`""", parse_mode="Markdown")
        elif message.text == "Удаленная касса":
            bot.send_message(message.chat.id, constants.uk1, parse_mode="Markdown")
          #  @bot.callback_query_handler(func=lambda call: True)
           # def answer(call):
               # if call.data == 'dalee':
            bot.send_message(message.chat.id, "При пробитии такого чека, возможно появление сообщения вида:")
            bot.send_photo(message.chat.id, photo='AgACAgIAAxkBAAILo2FOZlU_mPjUhaXSha6nax-FCthpAAIMtzEb8dhwSu6ArrZdGhuqAQADAgADeAADIQQ')
            bot.send_message(message.chat.id, """Смело выбираем НЕТ, чек сформируется и отправится клиенту при восстановлении связи.
`Важно: в момент отсутствия связи нельзя сбрасывать настройки ibox и обнулять кэш приложения, иначе
сохраненный черновик чека затрется до момента отправки!
В дальнейшем, в ibox будет добавлен счетчик отправленных чеков, чтобы видеть такие зависшие чеки.`""", parse_mode="Markdown")
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
        else:
            bot.send_message(message.chat.id, "пиши /start")
# ДЛЯ ГРУППЫ -----------------------------------------------------------------------------------------------------------
    elif message.chat.type == 'supergroup':
        if "работает" in message.text.lower() and "айбокс" in message.text.lower():
            bot.reply_to(message, "*Позвони в службу поддержки iBox +78003334526*", parse_mode="Markdown")
        elif "срочно" in message.text.lower():
            bot.send_message(message.chat.id, "*Запросы срочно обрабатываются в течение 5мин*", parse_mode="Markdown", disable_notification=True)
        elif "балл" in message.text.lower():
            bot.send_message(message.chat.id, "[Баллы Август Июль](https://docs.google.com/spreadsheets/d/1tFo0Fat2gachSWIWZKkqN_VU1xa7EhvuDmgMOewIzVg/edit#gid=1648712497)", parse_mode="Markdown")
            bot.send_message(message.chat.id, "[Баллы Октябрь Сентябрь](https://docs.google.com/spreadsheets/d/1-X9T4CkT8GP9xkLEiqj9IcX-gfS4AL_s1FNKO8m_ncQ/edit#gid=1127930766)", parse_mode="Markdown")
        elif message.text.lower() == "спасибо":
            bot.delete_message(message.chat.id, message.id)
        # КОСТИКА ------------------------
        elif "0 перенос" in message.text.lower() and "0 отмен" in message.text.lower() and "0 недоз" in message.text.lower():
            bot.reply_to(message, "Молодец!")
            reply = random.choice(constants.quality)
            bot.send_sticker(message.chat.id, reply)
        elif "0 отмен" in message.text.lower():
            bot.reply_to(message, "Проработай переносы!")
            bot.send_message(message.chat.id, constants.perenos, parse_mode="Markdown")
        elif "0 перенос" in message.text.lower() and "0 недоз" in message.text.lower():
            bot.reply_to(message, "Проработай отмены!, выясни причину!")
            bot.send_message(message.chat.id, constants.otmena, parse_mode="Markdown")
        elif "0 перенос" in message.text.lower() or "0 недоз" in message.text.lower():
            bot.reply_to(message, "Проработай переносы!")
            bot.send_message(message.chat.id, constants.perenos, parse_mode="Markdown")
        # КОСТИКА ------------------------
        elif "такси" in message.text.lower():
            bot.reply_to(message, "Группируемся по 4 человека в одном направлении, доступно 3 машины", parse_mode="Markdown")
        elif "дежурн" in message.text.lower():
            bot.reply_to(message, "*Дежурный СВ* +79160558030", parse_mode="Markdown")
        elif "мокка" in message.text.lower() or "рево" in message.text.lower():
            bot.reply_to(message, "*Мокка* +78007077236", parse_mode="Markdown")
        elif "механик" in message.text.lower() and "номер" in message.text.lower():
            bot.reply_to(message, "*Дежурный механик* +79150110787", parse_mode="Markdown")
        elif "лишн" in message.text.lower() and "вещ" in message.text.lower() or "лишн" in message.text.lower() and "позици" in message.text.lower() or "нет" in message.text.lower() and "позици" in message.text.lower() or "нет" in message.text.lower() and "вещ" in message.text.lower():
            bot.reply_to(message, """Проверяем *LMномер* позиции в заказе. Если нет - составляем бумажный акт на излишек.
`Посмотри внимательно, скорее всего 1 позиции в заказе не хватает электронный акт недостача`""", parse_mode="Markdown")
            bot.send_message(message.chat.id, "Бумажный акт")
            bot.send_photo(message.chat.id, photo='AgACAgIAAxkBAAIQrmFYsPYIPR5hUJx91rR2vHeOyK-4AAJWtDEb0R3JSgkNLQiFZJ_qAQADAgADeAADIQQ')
        elif "перен" in message.text.lower():
            bot.reply_to(message, "Проработай переносы!")
            bot.send_message(message.chat.id, constants.perenos, parse_mode="Markdown")
        elif "отмен" in message.text.lower():
            bot.reply_to(message, "Проработай отмены!, выясни причину!")
            bot.send_message(message.chat.id, constants.otmena, parse_mode="Markdown")
#    elif message.chat.type == 'group':
#        if "работает" in message.text.lower() and "айбокс" in message.text.lower():
#            bot.reply_to(message, "*Позвони в службу поддержки iBox +78003334526*", parse_mode="Markdown")
#        elif "срочно" in message.text.lower():
#            bot.send_message(message.chat.id, "*Запросы срочно обрабатываются в течение 5мин*", parse_mode="Markdown", disable_notification=True)
#        elif message.text.lower() == "спасибо":
#            bot.delete_message(message.chat.id, message.id)
#        elif "0 перенос" in message.text.lower() and "0 отмен" in message.text.lower() and "0 недоз" in message.text.lower():
#            bot.reply_to(message, "Молодец!")
#            reply = random.choice(constants.quality)
#            bot.send_sticker(message.chat.id, reply)
#        elif "0 отмен" in message.text.lower():
#            bot.reply_to(message, "Проработай переносы!")
#            bot.send_message(message.chat.id, constants.perenos, parse_mode="Markdown")
#        elif "0 перенос" in message.text.lower() and "0 недоз" in message.text.lower():
#            bot.reply_to(message, "Проработай отмены!, выясни причину!")
#            bot.send_message(message.chat.id, constants.otmena, parse_mode="Markdown")
#        elif "0 перенос" in message.text.lower() or "0 недоз" in message.text.lower():
#            bot.reply_to(message, "Проработай переносы!")
#            bot.send_message(message.chat.id, constants.perenos, parse_mode="Markdown")
#        elif "такси" in message.text.lower():
#            bot.reply_to(message, "Группируемся по 4 человека в одном направлении, доступно 3 машины", parse_mode="Markdown")


bot.polling()
