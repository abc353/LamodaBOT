import random
import requests
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
plansh_menu = types.InlineKeyboardMarkup()
da_plansh = types.InlineKeyboardButton("Могу вынуть аккумулятор\U0001F50B", callback_data='dabattery')
net_plansh = types.InlineKeyboardButton("Не могу вынуть, корпус цельный", callback_data='netbattery')
plansh_menu.add(da_plansh, net_plansh)
#меню Алгоритм работы с заказом. Переносы, отмены.
zakaz_menu = types.InlineKeyboardMarkup()
zakaz_button1 = types.InlineKeyboardButton("c клиентом", callback_data='s_klientom')
zakaz_button2 = types.InlineKeyboardButton("с вещью", callback_data='s_vesch')
zakaz_button3 = types.InlineKeyboardButton("с оборудованием", callback_data='s_oborud')
zakaz_button4 = types.InlineKeyboardButton("на маршруте", callback_data='s_marsh')
zakaz_button_exit = types.InlineKeyboardButton("Все ок\U0001F44C Я передумал", callback_data='zakaz_exit')
zakaz_menu.row(zakaz_button1, zakaz_button2, zakaz_button3)
zakaz_menu.row(zakaz_button4, zakaz_button_exit)
# КЛИЕНТ
klient = types.InlineKeyboardMarkup()
klient_button1 = types.InlineKeyboardButton("не может принять в интервал", callback_data='perenos_vr')
klient_button2 = types.InlineKeyboardButton("поменял пакеты", callback_data='pomenyal')
klient_button3 = types.InlineKeyboardButton("не отдает вещь\U000026A0", callback_data='neotdaet')
klient_button4 = types.InlineKeyboardButton("возврат", callback_data='vozvrat')
klient_button5 = types.InlineKeyboardButton("бумажный чек", callback_data='elchek')
klient_button6 = types.InlineKeyboardButton("дорогой 100000р", callback_data='more100000')
klient_button7 = types.InlineKeyboardButton("не отвечает на звонок", callback_data='nedozvon')
klient_button8 = types.InlineKeyboardButton("мультизаказы", callback_data='multi')
klient_button9 = types.InlineKeyboardButton("не открывает\U0001F6AA, 15мин", callback_data='neotkrivaet')
klient.row(klient_button8, klient_button2, klient_button3)
klient.row(klient_button4, klient_button5, klient_button6)
klient.row(klient_button7, klient_button1)
klient.row(klient_button9, zakaz_button_exit)
# ВЕЩЬ
vesch = types.InlineKeyboardMarkup()
vesch_button1 = types.InlineKeyboardButton("QRне сканируется", callback_data='qr')
vesch_button2 = types.InlineKeyboardButton("другая вещь", callback_data='drugves')
vesch_button3 = types.InlineKeyboardButton("брак", callback_data='brak')
vesch_button4 = types.InlineKeyboardButton("другой размер", callback_data='razmer')
vesch_button5 = types.InlineKeyboardButton("возврат", callback_data='vozvrat')
vesch_button6 = types.InlineKeyboardButton("поменял пакеты", callback_data='pomenyal')
vesch_button7 = types.InlineKeyboardButton("не подлежат возврату", callback_data='tovarivozvrat')
vesch_button8 = types.InlineKeyboardButton("не отдает вещь", callback_data='neotdaet')
vesch_button9 = types.InlineKeyboardButton("примерка запрещена\U0001F6AB", callback_data='bezprimerki')
vesch.row(vesch_button1, vesch_button2, vesch_button3)
vesch.row(vesch_button4, vesch_button5, vesch_button6)
vesch.row(vesch_button7, vesch_button8)
vesch.row(vesch_button9, zakaz_button_exit)
# ОБОРУДОВАНИЕ
oborudovan = types.InlineKeyboardMarkup()
oborudovan_but1 = types.InlineKeyboardButton("заказ остался на карте, чек пробил", callback_data='zavis')
oborudovan_but2 = types.InlineKeyboardButton("не включается планшет", callback_data='nevkl')
oborudovan_but3 = types.InlineKeyboardButton("не могу подключить ридер", callback_data='rider')
oborudovan_but4 = types.InlineKeyboardButton("не работает iBox", callback_data='ibox')
oborudovan_but6 = types.InlineKeyboardButton("завис Мокка", callback_data='mokka')
oborudovan_but7 = types.InlineKeyboardButton("Не проходит оплата", callback_data='oplata')
oborudovan.row(oborudovan_but1, oborudovan_but2)
oborudovan.row(oborudovan_but3, oborudovan_but4)
oborudovan.row(oborudovan_but6)
oborudovan.row(oborudovan_but7, zakaz_button_exit)
# МАРШРУТ
marsh = types.InlineKeyboardMarkup()
marsh_but1 = types.InlineKeyboardButton("адрес не полный", callback_data='nepoln')
marsh_but2 = types.InlineKeyboardButton("не успеваю к клиенту", callback_data='neuspevau')
marsh_but3 = types.InlineKeyboardButton("заказ остался на карте, чек пробил", callback_data='zavis')
marsh_but4 = types.InlineKeyboardButton("отмена", callback_data='otmena')
marsh_but5 = types.InlineKeyboardButton("перенос", callback_data='perenos')
marsh_but6 = types.InlineKeyboardButton("другой адрес", callback_data='adres')
marsh.row(marsh_but1, marsh_but2)
marsh.row(marsh_but6, marsh_but4, marsh_but5)
marsh.row(marsh_but3, zakaz_button_exit)






@bot.message_handler(commands='start')
def welcome(message):
    if message.chat.type == 'private':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIIQGFJQJ6aR-pSJuHPw2evH6cJJTOOAAJFAAN4qOYPxT4UDl0DPssgBA',
                         reply_markup=main_menu)
        bot.send_message(message.chat.id, "Привет, *" + message.chat.first_name +
                         "*. Это твое имя в телеграм для всех остальных. Переименуй его, если оно тебе не нравится и твои коллеги будут знать, как к тебе обращаться.\n"
                         "Бот ответит на большинство вопросов здесь или в [группе](https://t.me/joinchat/MzSkAJsKihA3ODU6).\n"
                         "Ниже используй кнопки для быстрой навигации по памяткам. Изучи их все!\U0001F447", parse_mode="Markdown")
    else:
        bot.reply_to(message, "Команды доступны только в л.с. боту. Пиши @lamodadedbot")

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
    else:
        bot.reply_to(message, "Команды доступны только в л.с. боту. Пиши @lamodadedbot")


@bot.message_handler(commands='gohome')
def handle_text(message):
    if message.chat.type == 'private':
        bot.reply_to(message, "Отправь мне свою Геопозицию \U0001F5FA. Нажми \U0001F4CE")
        @bot.message_handler(content_types='location')
        def handle_text(message):
            opa = message.location
            long = opa.longitude
            lat = opa.latitude
            longlat = str(long)+","+str(lat)
            PARAMS = {"apikey": "3a1f4689-5af6-4ae2-b912-208811535ee3", "lang": "ru_RU", "text": "Газпромнефть", "ll": longlat, "results": "2"}
            r = requests.get(url="https://search-maps.yandex.ru/v1/", params=PARAMS)
            json_data = r.json()
            latitude_address_str = json_data["features"][0]["geometry"]["coordinates"][1]
            longitude_address_str = json_data["features"][0]["geometry"]["coordinates"][0]
            bot.send_message(message.chat.id, "Ближайшая заправка Газпромнефть")
            bot.send_location(message.chat.id, latitude_address_str, longitude_address_str)
    else:
        bot.reply_to(message, "Команды доступны только в л.с. боту. Пиши @lamodadedbot")


@bot.message_handler(commands='help')
def handle_text(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, "`По всем возникающим вопросам прошу связаться` [со мной](https://t.me/dedovik).\n\n`При возникновении ошибки, неточности или при отсутствии ответа на запрос, прошу сообщить суть проблемы и приложить скриншот.`", parse_mode="Markdown")
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAIdYGFtK4gz9qzQpUPoOetTCt9137XXAALvAQACygMGC3h-hZvLvMChIQQ")
    else:
        bot.reply_to(message, "Команды доступны только в л.с. боту. Пиши @lamodadedbot")

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
        elif "отмен" in message.text.lower() or "перен" in message.text.lower() or "инфа" in message.text.lower() or "недозвон" in message.text.lower() or "примерк" in message.text.lower() or ("доп" in message.text.lower() and "номер" in message.text.lower()) or "проблем" in message.text.lower() or "возврат" in message.text.lower() or "брак" in message.text.lower() or "контакт" in message.text.lower() or "недоступ" in message.text.lower() or "подозрит" in message.text.lower() or "дорогой" in message.text.lower():
            bot.send_message(message.chat.id, text="*Не можешь доставить заказ? Возникла проблема с клиентом или на маршруте? Тупит планшет? \U0001F447Уточни:\U0001F447*", parse_mode="Markdown", reply_to_message_id=message.id, reply_markup=zakaz_menu)
            @bot.callback_query_handler(func=lambda call: call.data in ['zakaz_exit', 's_klientom', 's_vesch', 's_oborud', 's_marsh', 'pomenyal', 'neotdaet','neotkrivaet', 'vozvrat', 'qr', 'drugves', 'oplata', 'brak', 'razmer', 'elchek', 's_klientom_marsh', 'nedozvon', 'multi', 'perenos_vr', 'otmena', 'perenos', 'adres', 'bezprimerki', 'neuspevau', 'zavis','nepoln','mokka', 'nevkl', 'rider', 'oplatakarta', 'ibox', 'more100000','tovarivozvrat'])
            def callback_inline(call): #нужно добавить переменную id сообщения, чтобы менялось одно и то же сообщение ?
                if call.data == 's_klientom':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="*Что случилось?* \U0001F447*Клиент*\U0001F447", reply_markup=klient, parse_mode="Markdown")
                elif call.data == 's_vesch': #ВЕЩЬ
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="\U0001F447*Уточни проблему*\U0001F447", reply_markup=vesch, parse_mode="Markdown")
                elif call.data == 's_oborud':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="\U0001F447*Уточни проблему*\U0001F447", reply_markup=oborudovan, parse_mode="Markdown")
                elif call.data == 's_marsh':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="\U0001F447*Уточни проблему*\U0001F447", reply_markup=marsh, parse_mode="Markdown")
                elif call.data == 'more100000': #У КЛИЕНТА
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Свяжись с дежурным СВ до и после примерки. Необходимо _сообщить кол-во выкупленных позиций_, _сумму_, _метод оплаты_.\n\nПравила доставки ПК уточняй у [Бота](https://t.me/lamodadedbot). Пиши *Подозрительный клиент*", parse_mode="Markdown")
                elif call.data == 'pomenyal': #КЛИЕНТ
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Покажи клиенту, чем отличаются позиции. Сообщи, что продать позицию по ложной цене не сможешь.")
                elif call.data == 'neotdaet': #КЛИЕНТ
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="*Проверил позиции?* Попроси клиента вернуть вещь, которую ты *проверил* вместе с ним *ДО* примерки.\nНе отдает? Сообщи клиенту, что будешь вынужден вызвать полицию\U0001F693. При отказе звони дежурному СВ.\n\nКак проверить позиции уточняй у [Бота](https://t.me/lamodadedbot). Пиши *БПС*", parse_mode="Markdown")
                elif call.data == 'elchek': #КЛИЕНТ
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Lamoda отказалась от бумажных чеков. Чек придёт клиент на email, указанный при регистрации на сайте.\nЧек ничем не отличается от бумажного и при этом дольше хранится, безопасен для клиента и природы.\n\nВсе возражения смотри у [Бота](https://t.me/lamodadedbot). Пиши *Где бумажный чек?*", parse_mode="Markdown")
                elif call.data == 'neotkrivaet': #КЛИЕНТ
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Хочешь, чтобы клиент примерял вещи быстрее - договорись с клиентом *ДО* примерки о времени.\nПолучи ответ - обратную связь - согласие клиента.\nВидишь заранее, что клиент не уложится в 15мин - *договорись* о большем времени.\n\nЕсли КЛ пропал, не отвечает на звонки и не открывает дверь -  Сообщи дежурному СВ.\nБудь готов вызвать полицию\U0001F693.")
                elif call.data == 'vozvrat' or call.data == 'tovarivozvrat': #КЛИЕНТ
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Возврат *СТРОГО ЗАПРЕЩЕН*. Говори клиенту, что возврат доступен через ПВЗ.\n`Если ты все-таки сделал возврат и не можешь заново пробить позицию, то необходимо сбросить кэш и данные у приложения LmExpress`\n\nТакже смотри [Товары, не подлежащие возврату.](https://www.lamoda.ru/help/article/tovary-ne-podlezhashie-vozvratu-i-obmenu-ru/)", parse_mode="Markdown")
                elif call.data == 'qr': #КЛИЕНТ
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Включи вспышку. Ищи код на бирке, коробке, ярлыке. Вводи вручную символы под кодом.\nЕсли не удалось - пиши запрос в группу с номером позиции *LM123456789*", parse_mode="Markdown")
                elif call.data == 'drugves': #КЛИЕНТ
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Номер LM123456789 на прозрачном пакете совпадает с планшетом? - \U00002757Фиксируй *пересорт* в причине отказа\nПакета с таким номером нет в планшете - \U00002757Фиксируй *недостачу* в причине отказа и *излишек* на бумажном акте.\n\nКак заполнить бумажный акт уточняй у [Бота](https://t.me/lamodadedbot).", parse_mode="Markdown")
                elif call.data == 'oplata' or call.data == 'ibox': #КЛИЕНТ
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Убедись, что есть соединение с интернетом, iBox работает у твоих коллег, Cardreader корректно подключен к планшету.\nНе работает? - перезапусти оборудование.\n\nКак подключить ридер и номер iBox уточняй у [Бота](https://t.me/lamodadedbot", parse_mode="Markdown")
                elif call.data == 'brak': #КЛИЕНТ
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="\U00002757Фиксируй *брак* в причине отказа.\nНе забудь проинформировать клиента.", parse_mode="Markdown")
                elif call.data == 'razmer': #КЛИЕНТ
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Убедись, что размер совпадает с накладной и выбран в соответствие с размерной сеткой.\nНапример: Ботинок с отштамповкой *39* будет иметь *RU38* и *EU39*.\nЕсли размер не совпадает - \U00002757Фиксируй *пересорт* в причине отказа.", parse_mode="Markdown")
                elif call.data == 'nedozvon':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Убедись, что номер корректный. Если адрес полный - езжай до двери\U0001F6AA, если нет - запроси номер и адрес в КЦ.\nПродолжай попытки связи в течение дня.\n\n*Обязательно совершить минимум 3 звонка в интервал клиента не чаще, чем раз в 15мин.*", parse_mode="Markdown")
                elif call.data == 'multi':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Общая сумма свыше 100000р - сообщи дежурному супервайзеру и действую по правилам подозрительного клиента.\n\nПравила доставки ПК уточняй у [Бота](https://t.me/lamodadedbot). Пиши *Подозрительный клиент*", parse_mode="Markdown")
                elif call.data == 'perenos_vr' or call.data == 'neuspevau':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="*Договорись* с клиентом о доставке или о звонке позже *в течение дня*. Зафиксируй заказ, чтобы не было опоздания. Доставь заказ позже.\n\n`После можно перенести заказ в планшете день в день`", parse_mode="Markdown")
                elif call.data == 'otmena':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="*Отменяй заказ строго если:*\n\n"+constants.otmena, parse_mode="Markdown")
                elif call.data == 'perenos':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Действуй по пунктам:\n\n"+constants.perenos, parse_mode="Markdown")
                elif call.data == 'adres':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Выясни полный адрес. Не отказывай клиенту сразу, предложи доставку позже в течение дня. Позвони дежурному СВ для согласования доставки\n`Вполне возможно в конце смены появится окно. Если ты откажешь клиенту сразу, он перенесет заказ на другой день`", parse_mode="Markdown")
                elif call.data == 'bezprimerki':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="*Примерка партнерских заказов строго запрещена.* Заказы Lamoda по согласованию с дежурным СВ.\n\n`В отдельных случаях можно разрешить примерку и повлиять на выкуп для повышения общей лояльности клиента к компании.`", parse_mode="Markdown")
                elif call.data == 'nepoln':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Запиши всю информацию по адресу при первом звонке клиенту. Если клиент больше не отвечает - уточни адрес в КЦ или сделай запрос в чат. Езжай до двери\U0001F6AA")
                elif call.data == 'mokka':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Включи впн, обнови заказы. Позвони в Мокка, чтобы уточнить статус оплаты.\nКак включить впн и узнать номер Мокка ты можешь у [Бота](https://t.me/lamodadedbot). Пиши *впн* и *номер мокка*", parse_mode="Markdown")
                elif call.data == 'zavis':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=constants.bezcheka, parse_mode="Markdown")
                elif call.data == 'nevkl':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Пиши [Боту](https://t.me/lamodadedbot)- *как включить планшет*", parse_mode="Markdown")
                elif call.data == 'rider':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Пиши [Боту](https://t.me/lamodadedbot)- *как подключить ридер*", parse_mode="Markdown")
                elif call.data == 'zakaz_exit':
                    bot.delete_message(call.message.chat.id, call.message.id)

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
        elif "ibox" in message.text.lower() or "айбокс" in message.text.lower():
            bot.reply_to(message, "*Позвони в службу поддержки iBox +78003334526*", parse_mode="Markdown")
        elif "vpn" in message.text.lower() or "впн" in message.text.lower() or "connect" in message.text.lower():
            bot.send_animation(message.chat.id, animation=constants.vpn, caption="Добавляем сертификат")
        elif "подключить" in message.text.lower() and "ридер" in message.text.lower():
            photo2 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIUAAFhXWq_a4XctxVHDLvi-Zh0McuekwAC9rUxGzfi8UpW5N-ot69n9AEAAwIAA20AAyEE', caption="Заходим в iBox - Настройки - P17")
            photo3 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIUAWFdat_jon5RlxhJdd16uC0STsyNAAL3tTEbN-LxSu-cKoefkYRVAQADAgADbQADIQQ', caption="- Жмем на номер ридера")
            photo4 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIUAmFdavIDffCviWjuXY1iUvbztvRYAAL4tTEbN-LxSt_QLSu1ixVOAQADAgADbQADIQQ')
            photo1 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIT_2FdabvGkzEbrGsNpZX9xTcc28fJAAL0tTEbN-LxSqy5MNMeY6ymAQADAgADeAADIQQ', caption="Подключаем ридер к телефону через *Bluetooth*", parse_mode="Markdown")
            bot.send_media_group(message.chat.id, [photo1, photo2, photo3, photo4])
        elif "включить" in message.text.lower() and "планшет" in message.text.lower():
            bot.reply_to(message, "Можно вынуть АКБ?", reply_markup=plansh_menu)
            @bot.callback_query_handler(func=lambda call: call.data in ['dabattery', 'netbattery'])
            def callback_inline(call):
                if call.data == 'dabattery':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="\u0031\uFE0F\u20E3Вынь аккумулятор\n"
                                          "\u0032\uFE0F\u20E3Вставь кабель от сети в планшет\n"
                                          "\u0033\uFE0F\u20E3Дождись процентной индикации % заряда\n"
                                          "\u0034\uFE0F\u20E3Быстро вынь затем вставь заряжающий кабель")
                elif call.data == 'netbattery':
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Зажми и удерживай кнопки включения и \U00002795")
        else:
            bot.send_message(message.chat.id, "жми \U0001F449 /start \U0001F448 *памятки, инструкции*", parse_mode="Markdown")
            bot.send_message(message.chat.id, "жми \U0001F449 /new \U0001F448 *стажерам*", parse_mode="Markdown")
            bot.send_message(message.chat.id, "жми \U0001F449 /gohome \U0001F448 *навигация*", parse_mode="Markdown")
            bot.send_message(message.chat.id, "жми \U0001F449 /help \U0001F448 *обратная связь, контакты*", parse_mode="Markdown")
    # ДЛЯ ГРУППЫ -------------------------------------------------------------------------------------------------------
    elif message.chat.type == 'supergroup':
        if message.chat.title == "🚛Lamoda info👟" or message.chat.title == "Lamoda Dedovik":
            if "ibox" in message.text.lower() or "айбокс" in message.text.lower():
                bot.reply_to(message, "*Позвони в службу поддержки iBox +78003334526*", parse_mode="Markdown")
            elif "срочно" in message.text.lower():
                bot.send_message(message.chat.id, "*Запросы срочно обрабатываются в течение 5мин*", parse_mode="Markdown", disable_notification=True)
            elif "балл" in message.text.lower() and "мало" not in message.text.lower():
                bot.send_message(message.chat.id, "[Баллы Август Июль](https://docs.google.com/spreadsheets/d/1tFo0Fat2gachSWIWZKkqN_VU1xa7EhvuDmgMOewIzVg/edit#gid=1648712497)", parse_mode="Markdown")
                bot.send_message(message.chat.id, "[Баллы Октябрь Сентябрь](https://docs.google.com/spreadsheets/d/1=-X9T4CkT8GP9xkLEiqj9IcX-gfS4AL_s1FNKO8m_ncQ/edit#gid=1127930766)", parse_mode="Markdown")
            elif message.text.lower() == "спасибо":
                bot.delete_message(message.chat.id, message.id)
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
            elif "отмен" in message.text.lower() or "перен" in message.text.lower() or "инфа" in message.text.lower() or "недозвон" in message.text.lower() or "примерк" in message.text.lower() or ("доп" in message.text.lower() and "номер" in message.text.lower()) or "проблем" in message.text.lower() or "возврат" in message.text.lower() or "брак" in message.text.lower() or "контакт" in message.text.lower() or "недоступ" in message.text.lower() or "подозрит" in message.text.lower() or "дорогой" in message.text.lower():
                bot.send_message(message.chat.id, text="*Не можешь доставить заказ? Возникла проблема с клиентом или на маршруте? Тупит планшет? \U0001F447Уточни:\U0001F447*", parse_mode="Markdown", reply_to_message_id=message.id, reply_markup=zakaz_menu)
                @bot.callback_query_handler(func=lambda call: call.data in ['zakaz_exit', 's_klientom', 's_vesch', 's_oborud', 's_marsh', 'pomenyal', 'neotdaet','neotkrivaet', 'vozvrat', 'qr', 'drugves', 'oplata', 'brak', 'razmer', 'elchek', 's_klientom_marsh', 'nedozvon', 'multi', 'perenos_vr', 'otmena', 'perenos', 'adres', 'bezprimerki', 'neuspevau', 'zavis','nepoln','mokka', 'nevkl', 'rider', 'oplatakarta', 'ibox', 'more100000','tovarivozvrat'])
                def callback_inline(call): #нужно добавить переменную id сообщения, чтобы менялось одно и то же сообщение ?
                    if call.data == 's_klientom':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="*Что случилось?* \U0001F447*Клиент*\U0001F447", reply_markup=klient, parse_mode="Markdown")
                    elif call.data == 's_vesch': #ВЕЩЬ
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="\U0001F447*Уточни проблему*\U0001F447", reply_markup=vesch, parse_mode="Markdown")
                    elif call.data == 's_oborud':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="\U0001F447*Уточни проблему*\U0001F447", reply_markup=oborudovan, parse_mode="Markdown")
                    elif call.data == 's_marsh':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="\U0001F447*Уточни проблему*\U0001F447", reply_markup=marsh, parse_mode="Markdown")
                    elif call.data == 'more100000': #У КЛИЕНТА
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Свяжись с дежурным СВ до и после примерки. Необходимо _сообщить кол-во выкупленных позиций_, _сумму_, _метод оплаты_.\n\nПравила доставки ПК уточняй у [Бота](https://t.me/lamodadedbot). Пиши *Подозрительный клиент*", parse_mode="Markdown")
                    elif call.data == 'pomenyal': #КЛИЕНТ
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Покажи клиенту, чем отличаются позиции. Сообщи, что продать позицию по ложной цене не сможешь.")
                    elif call.data == 'neotdaet': #КЛИЕНТ
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="*Проверил позиции?* Попроси клиента вернуть вещь, которую ты *проверил* вместе с ним *ДО* примерки.\nНе отдает? Сообщи клиенту, что будешь вынужден вызвать полицию\U0001F693. При отказе звони дежурному СВ.\n\nКак проверить позиции уточняй у [Бота](https://t.me/lamodadedbot). Пиши *БПС*", parse_mode="Markdown")
                    elif call.data == 'elchek': #КЛИЕНТ
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Lamoda отказалась от бумажных чеков. Чек придёт клиент на email, указанный при регистрации на сайте.\nЧек ничем не отличается от бумажного и при этом дольше хранится, безопасен для клиента и природы.\n\nВсе возражения смотри у [Бота](https://t.me/lamodadedbot). Пиши *Где бумажный чек?*", parse_mode="Markdown")
                    elif call.data == 'neotkrivaet': #КЛИЕНТ
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Хочешь, чтобы клиент примерял вещи быстрее - договорись с клиентом *ДО* примерки о времени.\nПолучи ответ - обратную связь - согласие клиента.\nВидишь заранее, что клиент не уложится в 15мин - *договорись* о большем времени.\n\nЕсли КЛ пропал, не отвечает на звонки и не открывает дверь -  Сообщи дежурному СВ.\nБудь готов вызвать полицию\U0001F693.")
                    elif call.data == 'vozvrat' or call.data == 'tovarivozvrat': #КЛИЕНТ
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Возврат *СТРОГО ЗАПРЕЩЕН*. Говори клиенту, что возврат доступен через ПВЗ.\n`Если ты все-таки сделал возврат и не можешь заново пробить позицию, то необходимо сбросить кэш и данные у приложения LmExpress`\n\nТакже смотри [Товары, не подлежащие возврату.](https://www.lamoda.ru/help/article/tovary-ne-podlezhashie-vozvratu-i-obmenu-ru/)", parse_mode="Markdown")
                    elif call.data == 'qr': #КЛИЕНТ
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Включи вспышку. Ищи код на бирке, коробке, ярлыке. Вводи вручную символы под кодом.\nЕсли не удалось - пиши запрос в группу с номером позиции *LM123456789*", parse_mode="Markdown")
                    elif call.data == 'drugves': #КЛИЕНТ
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Номер LM123456789 на прозрачном пакете совпадает с планшетом? - \U00002757Фиксируй *пересорт* в причине отказа\nПакета с таким номером нет в планшете - \U00002757Фиксируй *недостачу* в причине отказа и *излишек* на бумажном акте.\n\nКак заполнить бумажный акт уточняй у [Бота](https://t.me/lamodadedbot).", parse_mode="Markdown")
                    elif call.data == 'oplata' or call.data == 'ibox': #КЛИЕНТ
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Убедись, что есть соединение с интернетом, iBox работает у твоих коллег, Cardreader корректно подключен к планшету.\nНе работает? - перезапусти оборудование.\n\nКак подключить ридер и номер iBox уточняй у [Бота](https://t.me/lamodadedbot", parse_mode="Markdown")
                    elif call.data == 'brak': #КЛИЕНТ
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="\U00002757Фиксируй *брак* в причине отказа.\nНе забудь проинформировать клиента.", parse_mode="Markdown")
                    elif call.data == 'razmer': #КЛИЕНТ
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Убедись, что размер совпадает с накладной и выбран в соответствие с размерной сеткой.\nНапример: Ботинок с отштамповкой *39* будет иметь *RU38* и *EU39*.\nЕсли размер не совпадает - \U00002757Фиксируй *пересорт* в причине отказа.", parse_mode="Markdown")
                    elif call.data == 'nedozvon':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Убедись, что номер корректный. Если адрес полный - езжай до двери\U0001F6AA, если нет - запроси номер и адрес в КЦ.\nПродолжай попытки связи в течение дня.\n\n*Обязательно совершить минимум 3 звонка в интервал клиента не чаще, чем раз в 15мин.*", parse_mode="Markdown")
                    elif call.data == 'multi':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Общая сумма свыше 100000р - сообщи дежурному супервайзеру и действую по правилам подозрительного клиента.\n\nПравила доставки ПК уточняй у [Бота](https://t.me/lamodadedbot). Пиши *Подозрительный клиент*", parse_mode="Markdown")
                    elif call.data == 'perenos_vr' or call.data == 'neuspevau':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="*Договорись* с клиентом о доставке или о звонке позже *в течение дня*. Зафиксируй заказ, чтобы не было опоздания. Доставь заказ позже.\n\n`После можно перенести заказ в планшете день в день`", parse_mode="Markdown")
                    elif call.data == 'otmena':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="*Отменяй заказ строго если:*\n\n"+constants.otmena, parse_mode="Markdown")
                    elif call.data == 'perenos':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Действуй по пунктам:\n\n"+constants.perenos, parse_mode="Markdown")
                    elif call.data == 'adres':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Выясни полный адрес. Не отказывай клиенту сразу, предложи доставку позже в течение дня. Позвони дежурному СВ для согласования доставки\n`Вполне возможно в конце смены появится окно. Если ты откажешь клиенту сразу, он перенесет заказ на другой день`", parse_mode="Markdown")
                    elif call.data == 'bezprimerki':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="*Примерка партнерских заказов строго запрещена.* Заказы Lamoda по согласованию с дежурным СВ.\n\n`В отдельных случаях можно разрешить примерку и повлиять на выкуп для повышения общей лояльности клиента к компании.`", parse_mode="Markdown")
                    elif call.data == 'nepoln':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Запиши всю информацию по адресу при первом звонке клиенту. Если клиент больше не отвечает - уточни адрес в КЦ или сделай запрос в чат. Езжай до двери\U0001F6AA")
                    elif call.data == 'mokka':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Включи впн, обнови заказы. Позвони в Мокка, чтобы уточнить статус оплаты.\nКак включить впн и узнать номер Мокка ты можешь у [Бота](https://t.me/lamodadedbot). Пиши *впн* и *номер мокка*", parse_mode="Markdown")
                    elif call.data == 'zavis':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=constants.bezcheka, parse_mode="Markdown")
                    elif call.data == 'nevkl':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Пиши [Боту](https://t.me/lamodadedbot)- *как включить планшет*", parse_mode="Markdown")
                    elif call.data == 'rider':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Пиши [Боту](https://t.me/lamodadedbot)- *как подключить ридер*", parse_mode="Markdown")
                    elif call.data == 'zakaz_exit':
                        bot.delete_message(call.message.chat.id, call.message.id)

            elif "vpn" in message.text.lower() or "впн" in message.text.lower() or "connect" in message.text.lower():
                bot.send_animation(message.chat.id, animation=constants.vpn, caption="Добавляем сертификат")
            elif "подключить" in message.text.lower() and "ридер" in message.text.lower():
                photo2 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIUAAFhXWq_a4XctxVHDLvi-Zh0McuekwAC9rUxGzfi8UpW5N-ot69n9AEAAwIAA20AAyEE', caption="Заходим в iBox - Настройки - P17")
                photo3 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIUAWFdat_jon5RlxhJdd16uC0STsyNAAL3tTEbN-LxSu-cKoefkYRVAQADAgADbQADIQQ', caption="- Жмем на номер ридера")
                photo4 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIUAmFdavIDffCviWjuXY1iUvbztvRYAAL4tTEbN-LxSt_QLSu1ixVOAQADAgADbQADIQQ')
                photo1 = types.InputMediaPhoto(media='AgACAgIAAxkBAAIT_2FdabvGkzEbrGsNpZX9xTcc28fJAAL0tTEbN-LxSqy5MNMeY6ymAQADAgADeAADIQQ', caption="Подключаем ридер к телефону через *Bluetooth*", parse_mode="Markdown")
                bot.send_media_group(message.chat.id, [photo1, photo2, photo3, photo4])
            elif "включить" in message.text.lower() and "планшет" in message.text.lower():
                bot.reply_to(message, "Можно вынуть АКБ?", reply_markup=plansh_menu)
                @bot.callback_query_handler(func=lambda call: call.data in ['dabattery', 'netbattery'])
                def callback_inline(call):
                    if call.data == 'dabattery':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="\u0031\uFE0F\u20E3Вынь аккумулятор\n"
                                              "\u0032\uFE0F\u20E3Вставь кабель от сети в планшет\n"
                                              "\u0033\uFE0F\u20E3Дождись процентной индикации % заряда\n"
                                              "\u0034\uFE0F\u20E3Быстро вынь затем вставь заряжающий кабель")
                    elif call.data == 'netbattery':
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Зажми и удерживай кнопки включения и \U00002795")
        elif message.chat.title == "LMF":
        # КОСТИКА ------------------------
            if "0 перенос" in message.text.lower() and "0 отмен" in message.text.lower() and "0 недоз" in message.text.lower():
                bot.reply_to(message, "Молодец!")
                reply = random.choice(constants.quality)
                bot.send_sticker(message.chat.id, reply)
            # elif "0 отмен" in message.text.lower():
            #     bot.reply_to(message, "Проработай переносы!")
            # elif "0 перенос" in message.text.lower() and "0 недоз" in message.text.lower():
            #     bot.reply_to(message, "Проработай отмены!, выясни причину!")
            # elif "0 перенос" in message.text.lower() or "0 недоз" in message.text.lower():
            #     bot.reply_to(message, "Проработай переносы!")
        # КОСТИКА ------------------------
        else:
            bot.send_message(message.chat.id, "Некорректная группа\U000026D4")



bot.polling()
