import random

import telebot
import constants
from telebot import types

bot = telebot.TeleBot(constants.token)
main_menu = types.ReplyKeyboardMarkup(True)
main_menu.row('Заказ,Оплата,Опоздания,Нет соединения')
main_menu.row('Где бумажный чек?', 'Памятки')
main_menu.row('Контактная информация', 'Где мой промокод')
menu_pravila = types.ReplyKeyboardMarkup(True)
menu_pravila.row('Как мне работать с отменами и переносами?')
menu_pravila.row('Когда отменять заказ?', 'Не успеваю в интервал')
menu_pravila.row('Заказ остался на карте', 'Не прошла оплата')
menu_pravila.row('Нет соединения, Anyconnect', 'Планшет не включается')
menu_pravila.row('Главное меню')
menu_pamyatki = types.ReplyKeyboardMarkup(True)
menu_pamyatki.row('БПС', 'Удаленная касса')
menu_pamyatki.row('Подозрительный клиент')
menu_pamyatki.row('Главное меню')
menu_stop = types.ReplyKeyboardRemove()
new_menu1 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Что дальше?', callback_data='1')
new_menu1.add(button1)
new_menu2 = types.InlineKeyboardMarkup()
button2 = types.InlineKeyboardButton('Я готов\U0001F44D', callback_data='2')
new_menu2.add(button2)
new_menu3 = types.InlineKeyboardMarkup()
button3 = types.InlineKeyboardButton('Все взял\U0001F44D Хочу работать', callback_data='3')
new_menu3.add(button3)
new_menu4 = types.InlineKeyboardMarkup()
button4 = types.InlineKeyboardButton('\U00002757Теперь уже точно все\U00002757', callback_data='4')
new_menu4.add(button4)


@bot.message_handler(commands='start')
def welcome(message):
    if message.chat.type == 'private':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIIQGFJQJ6aR-pSJuHPw2evH6cJJTOOAAJFAAN4qOYPxT4UDl0DPssgBA',
                         reply_markup=main_menu)
        bot.send_message(message.chat.id, "Привет, *" + message.chat.first_name +
                         "*. Это твое имя в телеграм для всех остальных. Переименуй его, если оно тебе не нравится и твои коллеги будут знать, как к тебе обращаться.\n"
                         "Бот ответит на большинство вопросов здесь или в [группе](https://t.me/joinchat/MzSkAJsKihA3ODU6).\n"
                         "Ниже используй кнопки для быстрой навигации по памяткам. Изучи их все!\U0001F447", parse_mode="Markdown")


@bot.message_handler(commands='new')
def handle_text(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, "*" + message.chat.first_name + "*, обязательно изучи все памятки и инструкции. Жми \U0001F449 /start \U0001F448.", parse_mode="Markdown", reply_markup=new_menu1)
        @bot.callback_query_handler(func=lambda call: call.data in ['1', '2', '3', '4'])
        def callback_inline(call):
            if call.data == '1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Внимательно изучи [СТАНДАРТНЫЙ НАБОР ОПЕРАЦИЙ ТОРГОВОГО ПРЕДСТАВИТЕЛЯ](https://drive.google.com/file/d/19TFv_5iqnTdJK_bfFS8hW7ivFIcGyACp/view?usp=sharing)\n"
                                      "В нем подробно расписан твой день, начиная с подготовки к маршруту, заканчивая вечерней приемкой.", parse_mode="Markdown", reply_markup=new_menu2)
            elif call.data == '2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Возьми с собой:\n"
                                      "\u0031\uFE0F\u20E3Зарядное устройство в прикуриватель или powerbank\n"
                                      "\u0032\uFE0F\u20E3Type-C и MicroUSB провода для зарядки\n"
                                      "\u0033\uFE0F\u20E3Ручки и акты несоответствия. `Можно получить с утра у СВ`\n"
                                      "\u0034\uFE0F\u20E3Гарнитуру или наушник\n"
                                      "\u0035\uFE0F\u20E3Фирменные пакеты Lamoda для клиентов"
                                      , parse_mode="Markdown", reply_markup=new_menu3)
            elif call.data == '3':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Приведи в порядок внешний вид:\n"
                                      "\u0031\uFE0F\u20E3Получи форму у своего СВ\n"
                                      "\u0032\uFE0F\u20E3Выгляди опрятно и ухоженно\n"
                                      "\u0033\uFE0F\u20E3Одень темные джинсы\n"
                                      "\u0034\uFE0F\u20E3Получи бейдж-пропуск с твоим именем"
                                      , parse_mode="Markdown", reply_markup=new_menu4)
            elif call.data == '4':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Подожди, ты уже получил QR код и логин+пароль iBox для работы? Напомни своему супервайзеру прислать их\n"
                                      "И не забывай про памятки и инструкции \U0001F449 /start \U0001F448, а также бота, который ответит на все вопросы, например *номер кол центра*", parse_mode="Markdown")




@bot.message_handler(commands='gohome')
def handle_text(message):
    if message.chat.type == 'private':
        bot.send_location(message.chat.id, 55.728270423944274, 37.7148733308119)




@bot.message_handler(content_types='text')
def handle_text(message):
    # матный фильтр
    for i in constants.mat:
        if i in message.text.lower():
            bot.delete_message(message.chat.id, message.id)
            bot.send_message(message.chat.id, str(message.from_user.first_name) + ", предупреждение!\U0001F6AB")
            bot.send_message(message.chat.id, "\U0001F910 `ненормативная лексика запрещена`\U0001F910 ", parse_mode="Markdown")
            message.text = " "
    # матный фильтр
    # ДЛЯ БОТА ---------------------------------------------------------------------------------------------------------
    if message.chat.type == 'private':
        if message.text == "Контактная информация":
            bot.send_message(message.chat.id, constants.contact, parse_mode="Markdown")
        elif message.text == "Где мой промокод":
            bot.send_message(message.chat.id, constants.promokod, parse_mode="Markdown")
        elif message.text == "Где бумажный чек?":
            bot.send_message(message.chat.id, constants.elchek, parse_mode="Markdown")
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
            bot.send_message(message.chat.id, "При пробитии такого чека, возможно появление сообщения вида:")
            bot.send_photo(message.chat.id, photo='AgACAgIAAxkBAAILo2FOZlU_mPjUhaXSha6nax-FCthpAAIMtzEb8dhwSu6ArrZdGhuqAQADAgADeAADIQQ')
            bot.send_message(message.chat.id, """Смело выбираем НЕТ, чек сформируется и отправится клиенту при 
восстановлении связи. `Важно: в момент отсутствия связи нельзя сбрасывать настройки ibox и обнулять кэш 
приложения, иначе сохраненный черновик чека затрется до момента отправки! В дальнейшем, в ibox будет 
добавлен счетчик отправленных чеков, чтобы видеть такие зависшие чеки.`""", parse_mode="Markdown")
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
        elif "дежурн" in message.text.lower() and "механик" not in message.text.lower():
            bot.reply_to(message, "*Дежурный СВ* +79160558030", parse_mode="Markdown")
        elif "мокка" in message.text.lower() or "мокко" in message.text.lower():
            bot.reply_to(message, "*Мокка* +78007077236", parse_mode="Markdown")
        elif "механик" in message.text.lower() and "номер" in message.text.lower():
            bot.reply_to(message, "*Дежурный механик* +79150110787", parse_mode="Markdown")
        elif "КЦ" in message.text or (("номер" in message.text.lower() or "звонит" in message.text.lower()) and "центр" in message.text.lower()):
            bot.reply_to(message, "*Call Центр* +74995004959", parse_mode="Markdown")
        elif "лишн" in message.text.lower() and "вещ" in message.text.lower() or "лишн" in message.text.lower() and "позици" in message.text.lower() or "нет" in message.text.lower() and "позици" in message.text.lower() or "нет" in message.text.lower() and "вещ" in message.text.lower():
            bot.reply_to(message, "Заполняем бумажный акт")
            bot.send_photo(message.chat.id, photo='AgACAgIAAxkBAAIQrmFYsPYIPR5hUJx91rR2vHeOyK-4AAJWtDEb0R3JSgkNLQiFZJ_qAQADAgADeAADIQQ',
                           caption="""Проверяем *LMномер* позиции в заказе. Если нет - составляем бумажный акт на излишек.
`Посмотри внимательно, скорее всего 1 позиции в заказе не хватает электронный акт недостача`""",
                           parse_mode="Markdown")
        elif "акт" in message.text.lower() and "несоответ" in message.text.lower():
            bot.send_photo(message.chat.id,
                           photo='AgACAgIAAxkBAAIQrmFYsPYIPR5hUJx91rR2vHeOyK-4AAJWtDEb0R3JSgkNLQiFZJ_qAQADAgADeAADIQQ',
                           caption="Бумажный акт несоответствия")
        elif "балл" in message.text.lower() and "мало" not in message.text.lower():
            bot.send_message(message.chat.id, "[Баллы Август Июль](https://docs.google.com/spreadsheets/d/1tFo0Fat2gachSWIWZKkqN_VU1xa7EhvuDmgMOewIzVg/edit#gid=1648712497)", parse_mode="Markdown")
            bot.send_message(message.chat.id, "[Баллы Октябрь Сентябрь](https://docs.google.com/spreadsheets/d/1-X9T4CkT8GP9xkLEiqj9IcX-gfS4AL_s1FNKO8m_ncQ/edit#gid=1127930766)", parse_mode="Markdown")
        elif "работает" in message.text.lower() and "айбокс" in message.text.lower():
            bot.reply_to(message, "*Позвони в службу поддержки iBox +78003334526*", parse_mode="Markdown")
        elif "vpn" in message.text.lower() or "впн" in message.text.lower() or "connect" in message.text.lower():
            bot.send_animation(message.chat.id, animation=constants.vpn, caption="Добавляем сертификат")
        elif "подключить" in message.text.lower() and "ридер" in message.text.lower():
            photo2 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIUAAFhXWq_a4XctxVHDLvi-Zh0McuekwAC9rUxGzfi8UpW5N-ot69n9AEAAwIAA20AAyEE', caption="Заходим в iBox - Настройки - P17")
            photo3 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIUAWFdat_jon5RlxhJdd16uC0STsyNAAL3tTEbN-LxSu-cKoefkYRVAQADAgADbQADIQQ', caption="- Жмем на номер ридера")
            photo4 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIUAmFdavIDffCviWjuXY1iUvbztvRYAAL4tTEbN-LxSt_QLSu1ixVOAQADAgADbQADIQQ')
            photo1 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIT_2FdabvGkzEbrGsNpZX9xTcc28fJAAL0tTEbN-LxSqy5MNMeY6ymAQADAgADeAADIQQ', caption="Подключаем ридер к телефону через *Bluetooth*", parse_mode="Markdown")
            bot.send_media_group(message.chat.id, [photo1, photo2, photo3, photo4])
        else:
            bot.send_message(message.chat.id, "нажми \U0001F449 /start \U0001F448, раздел памятки")
            bot.send_message(message.chat.id, "нажми \U0001F449 /new \U0001F448, раздел для стажеров")
            bot.send_message(message.chat.id, "нажми \U0001F449 /gohome \U0001F448, для навигации")
    # ДЛЯ ГРУППЫ -------------------------------------------------------------------------------------------------------
    elif message.chat.type == 'supergroup':
        if "работает" in message.text.lower() and "айбокс" in message.text.lower():
            bot.reply_to(message, "*Позвони в службу поддержки iBox +78003334526*", parse_mode="Markdown")
        elif "срочно" in message.text.lower():
            bot.send_message(message.chat.id, "*Запросы срочно обрабатываются в течение 5мин*", parse_mode="Markdown", disable_notification=True)
        elif "балл" in message.text.lower() and "мало" not in message.text.lower():
            bot.send_message(message.chat.id, "[Баллы Август Июль](https://docs.google.com/spreadsheets/d/1tFo0Fat2gachSWIWZKkqN_VU1xa7EhvuDmgMOewIzVg/edit#gid=1648712497)", parse_mode="Markdown")
            bot.send_message(message.chat.id, "[Баллы Октябрь Сентябрь](https://docs.google.com/spreadsheets/d/1=-X9T4CkT8GP9xkLEiqj9IcX-gfS4AL_s1FNKO8m_ncQ/edit#gid=1127930766)", parse_mode="Markdown")
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
        elif "дежурн" in message.text.lower() and "механик" not in message.text.lower():
            bot.reply_to(message, "*Дежурный СВ* +79160558030", parse_mode="Markdown")
        elif "мокка" in message.text.lower() or "мокко" in message.text.lower():
            bot.reply_to(message, "*Мокка* +78007077236", parse_mode="Markdown")
        elif "механик" in message.text.lower() and "номер" in message.text.lower():
            bot.reply_to(message, "*Дежурный механик* +79150110787", parse_mode="Markdown")
        elif "КЦ" in message.text or (("номер" in message.text.lower() or "звонит" in message.text.lower()) and "центр" in message.text.lower()):
            bot.reply_to(message, "*Call Центр* +74995004959", parse_mode="Markdown")
        elif "лишн" in message.text.lower() and "вещ" in message.text.lower() or "лишн" in message.text.lower() and "позици" in message.text.lower() or "нет" in message.text.lower() and "позици" in message.text.lower() or "нет" in message.text.lower() and "вещ" in message.text.lower():
            bot.reply_to(message, "Заполняем бумажный акт")
            bot.send_photo(message.chat.id, photo='AgACAgIAAxkBAAIQrmFYsPYIPR5hUJx91rR2vHeOyK-4AAJWtDEb0R3JSgkNLQiFZJ_qAQADAgADeAADIQQ',
                           caption="""Проверяем *LMномер* позиции в заказе. Если нет - составляем бумажный акт на излишек.
`Посмотри внимательно, скорее всего 1 позиции в заказе не хватает электронный акт недостача`""",
                           parse_mode="Markdown")
        elif "акт" in message.text.lower() and "несоответ" in message.text.lower():
            bot.send_photo(message.chat.id,
                           photo='AgACAgIAAxkBAAIQrmFYsPYIPR5hUJx91rR2vHeOyK-4AAJWtDEb0R3JSgkNLQiFZJ_qAQADAgADeAADIQQ',
                           caption="Бумажный акт несоответствия")
        elif "перен" in message.text.lower():
            bot.reply_to(message, "Проработай переносы!")
            bot.send_message(message.chat.id, constants.perenos, parse_mode="Markdown")
        elif "отмен" in message.text.lower():
            bot.reply_to(message, "Проработай отмены!, выясни причину!")
            bot.send_message(message.chat.id, constants.otmena, parse_mode="Markdown")
        elif "vpn" in message.text.lower() or "впн" in message.text.lower() or "connect" in message.text.lower():
            bot.send_animation(message.chat.id, animation=constants.vpn, caption="Добавляем сертификат")
        elif "подключить" in message.text.lower() and "ридер" in message.text.lower():
            photo2 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIUAAFhXWq_a4XctxVHDLvi-Zh0McuekwAC9rUxGzfi8UpW5N-ot69n9AEAAwIAA20AAyEE', caption="Заходим в iBox - Настройки - P17")
            photo3 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIUAWFdat_jon5RlxhJdd16uC0STsyNAAL3tTEbN-LxSu-cKoefkYRVAQADAgADbQADIQQ', caption="- Жмем на номер ридера")
            photo4 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIUAmFdavIDffCviWjuXY1iUvbztvRYAAL4tTEbN-LxSt_QLSu1ixVOAQADAgADbQADIQQ')
            photo1 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIT_2FdabvGkzEbrGsNpZX9xTcc28fJAAL0tTEbN-LxSqy5MNMeY6ymAQADAgADeAADIQQ', caption="Подключаем ридер к телефону через *Bluetooth*", parse_mode="Markdown")
            bot.send_media_group(message.chat.id, [photo1, photo2, photo3, photo4])


bot.polling()
