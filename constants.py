token = "5584155755:AAGkzO-rjenPQF9Qov3U_y19hkrvhiWrnC4"
vpn = 'CgACAgIAAxkBAAIH1GFJK3uBEM69kSfWNxCinKG2XC6JAAINDgAClexRSgOcbRmSsJyZIAQ'
bps = 'CgACAgIAAxkBAAILP2FOWTxLvFr9piR4GgaP9EUt55YOAALOEAAC8dhwSumWIL4WwL0yIQQ'
mat = ["бля", "хуй", "сука", "ебат", "пизд", "наебал", "ебал", "ебан", "заеб", "хуя", "жоп", "пидор"]
quality = ['CAACAgIAAxkBAAN-YVBRlXDf8B_UQxMruBM4zuGjAVUAAjkAA2dmzAZUvY8kyWS4BCEE',
'CAACAgEAAxkBAAN_YVBR-kHlnsVLo89cVMBll6mWqEMAArEIAAK_jJAEZc7fLyeQzjYhBA',
'CAACAgIAAxkBAAOAYVBSa7pmdMhSbu0Up0BeOQhv_KgAAj0AAxgkOQ4JqIFwUJ3f-CEE',
'CAACAgIAAxkBAAOBYVBSiz9p-1OtmVI9Le77u9FSp6kAAn8LAAKlHwFK60vZpBb_NdchBA',
'CAACAgIAAxkBAAOCYVBSqUJS9B-wA1SpbYlfZ3Et7DgAAkMAA2dmzAabjEh2IzuKWSEE',
'CAACAgIAAxkBAAODYVBSubDqahDnvH88Yk9ppDzXz38AAn0BAAI9DegE0tx32kuSOTQhBA',
'CAACAgIAAxkBAAOEYVBSzFhzzSaPqoc9uFJsjxfhws0AAnoAA_19Gh7V85f4RvblcyEE',
'CAACAgIAAxkBAAOFYVBURPCauKN9RO9krYgQdWotAfAAAgsDAAJtsEIDf7Qc2symRCUhBA',
'CAACAgIAAxkBAAOHYVBVJ_EpSXolZ9tbpwgsJmMMFhMAAtoBAAI9DegE2zGxPaKQrUQhBA',
'CAACAgIAAxkBAAOdYVBWFPQIkjO9bDnvxual5pFl1wYAAnkAA4_0DAABmHm2JKAD_QABIQQ']
perenos = """\u0031\uFE0F\u20E3- Выясни причину
\u0032\uFE0F\u20E3 - Предложи доставку заказа в другой интервал сегодня же
\u0033\uFE0F\u20E3 - Предложи доставку по другому адресу, главное чтобы клиент принял сегодня `адрес согласовываем с супервайзером`
\u0034\uFE0F\u20E3 - Предложи оставить заказ у родственников/друзей/консъержа (если заказ не оплачен, предложи перевод на карту или оплату от родственников/друзей/консъержа)
‼‼‼ - Покажи гибкость и лояльность компании, используя каждый раз все 4 пункта.
`так ты точно поймешт, нужен ли заказ клиенту`"""
otmena = """Узнай у клиента причину отмены заказа. *Заказ клиенту нужен?* - согласуй перенос.
*Не нужен?* - действуй по пунктам:
\u0031\uFE0F\u20E3 - Отмена по просьбе клиента `крайне желательно подтверждение отмены по рабочему телефону в звонке`
\u0032\uFE0F\u20E3 - У заказа последняя-3я попытка доставки `смотрим через статус недозвон или в маршрутном листе`
\u0032\uFE0F\u20E3.\u0031\uFE0F\u20E3 - У заказа кончаются дни хранения на складе. Всего 5 дней
`если у вас 3 дня хранения, то перенести можно на завтра или послезавтра`
\u0033\uFE0F\u20E3 - Фактический адрес доставки не входит в зону Южного склада. `уточняем у супервайзера`
*Только оформление нового заказа с корректным адресом. Перенос невозможен*"""
contact = """*Call Центр* +74995004959
*Дежурный СВ* +79160558030
*Дежурный механик* +79150110787
*Дежурный кассир* +79175805523
*Паркоматика* +78003015748
*Мокка* +78007077236
*iboxPro* +78003334526
*СБ* +79999991489"""
promokod = """Для получения promo-кода зарегистрируйся в приложении лямоды, используя логин *iBox*
`номер телефона должен совпадать с указанным в отделе кадров`, """
opozdanie = """Сообщи, что опаздываешь до окончания интервала доставки.

*Договорись* с клиентом о доставке или о звонке позже *в течение дня*. Зафиксируй заказ, чтобы не было опоздания.
`После можно перенести заказ в планшете день в день`

Доставь заказ позже. Если не смог дозвониться в конце смены - ставь *недозвон*.

Как убрать опоздание - пиши в группу *без опоздания*"

Примеры:

_Анна Петровна, LMexp, ТП Александр, чуть задерживаюсь к Вам. Было бы Вам удобно принять заказ позже 12?_ `интервал до 12`

_Анна Петровна, меня зовут Александр, доставляю Ваш заказ от Lamoda, возможно не успею в интервал до 12. Могли бы Вы пойти на встречу и принять заказ в удобное для Вас время позже?_"""
bezcheka = """*Клиент оплатил, а заказ остался на карте?*
Проверь успешность платежа в iBox.
Зайди в iBox, открой историю продаж, найди чек с нужной суммой. Напротив сумму смотри статус.

*Успешен?* `уходим от клиента`
Отметь все позиции, которые выбрал клиент. Выбери тот же способ оплаты, нажми *₽*. Не пробивай чек, жми кнопку↩️. Отменяй. Жми Продолжить. Закрыть без чека.
Обнови заказы. Продолжи маршрут\U0001F44C.

*Если чек отсутствует в iBox - закрывать заказ без чека СТРОГО ЗАПРЕЩЕНО*
`если заказ вернулся на карту, оставь так`"""
oplata = """🔸Проверь, что деньги поступили в ламоду.

🔸Зайди в *iBox* история платежей. Потяни вниз - обновится список платежей. `должно быть соединение с интернетом`
Сверху будет твой послендний заказ. Открой его, слева внизу (напротив суммы платежа) найди *Платеж успешен*
Если платежа нет или он не успешен - *Деньги Не Поступили - Проведи оплату заново!*

`Как убрать заказ с карты уточняй у `[Бота](https://t.me/lamodadedbot). *Пиши - проблема*"""
#- Обновляем все заказы, заходим в настройки телефона.
#`меню - приложения - Lmexpess mobile - Память - Очистить кэш и данные`
#Заходим заново Lmexpess mobile, в заказах списком находим клиента, жмем корзинку
anyconnect = """Добавляем сертификат"""
elchek = """*А где бумажный чек?*\U0001F9FE

_Lamoda отказывается от бумажных чеков при доставке, ваш чек придёт к вам на ваш адрес электронной почты, который вы указывали при регистрации у нас на сайте.
Он ничем не отличается от бумажного и при этом дольше хранится, безопасен для вас и природы._

*Почему электронный?*

_Мы работаем над тем, чтобы наш сервис был безопасен для вас и окружающей среды, современен, удобен и экономичен.
В электронном виде чеки:
    ·можно хранить бесконечно долго – бумажные выцветают и стираются, не позволяя вести длительный учёт своих покупок.
    ·не вредят окружающей среде – кассовая лента производится с применением различных химикатов из-за них её нельзя перерабатывать, как обычную бумагу.
    ·не вредят здоровью – в составе кассовой ленты могут входить вредные соединения (Бисфенол-А), негативно влияющие на здоровье.
    ·делают наш сервис современнее и удобнее – большинство крупных интернет-магазинов и маркетплейсов уже перешли на электронные чеки при доставке.
    ·позволяют нам сфокусироваться на доставке для вас – не придётся ждать пока распечатается чек (подвисла), заработает касса (зависла), заменится аккумулятор (сломалась) или появится Галя с отменой (что-то пошло не так!) 😉_

*А он точно настоящий?*

_Электронный чек ничем не отличается от бумажного, в нём есть все параметры, описанные в законе.
Интернет-магазин и службы доставки могут отправлять только электронные чеки без печати бумажной копии - это закреплено в законе (54 ФЗ).
Его правильность, вы всегда можете проверить на сайте nalog.ru, либо воспользоваться мобильным приложение ФНС для проверки чеков._

*А в личном кабинете Lamoda чеки будут, как у «ZZZ»?*

_Обязательно будет, но позже (точные сроки не говорим)._

*А при доставке у XXX печатают чек!*

_Большинство доставок (X5, вкусвилл, Ситилинк, OZON, Wildberries и другие) уже перешли на электронные чеки в доставке и уже уменьшают количество печатных чеков в магазинах и точках выдачи.
Скорее всего и XXX скоро переключится на электронные чеки – это часть прогресса и требования закона._

*А в YYY мне привозят заказ с заранее напечатанным чеком!*

_Мы соблюдаем Российское законодательство – по нему так делать нельзя и за это обязательно будет штраф. Чек должен появиться в момент расчёта или передачи товара._

*А вдруг я его не получу!*

Если что-то пошло не так, наша служба поддержки поможет найти чек и предоставит его в частном порядке. В интересах Lamoda оправдать ваше доверие и не нарушить закон.

*А я хочу бумажный! Я юрист и знаю законы! Дайте бумажный чек!*

_Вы можете распечатать электронный чек на принтере, сохранить как картинку, документ или добавить чек в приложение налоговой службы. Во всех случаях – это будет один и тот же чек, имеющий одинаковую юридическую силу.
Передавая чек в электронной форме клиенту, мы полностью выполняем требования Федерального закона от 22.05.2003 N 54-ФЗ «О применении контрольно-кассовой техники»._"""
pk = """Действия торгового представителя:
- по прибытии в адрес доставки необходимо осмотреть территорию `желательно сделать круг на ТС`,
обращать внимание на группы лиц, находящихся в непосредственной близости; припаркованные ТС с лицами в салоне и т.д.;
- произвести парковку в максимально освещенном и просматриваемом месте,
по возможности в непосредственной близости от препятствий, затрудняющих доступ  ТС;
- осмотреться по зеркалам;
- созвониться с клиентом и уточнить детали доставки
`желательно спросить пару контрольных вопросов по ориентированию в районе доставки, код домофона, этажность здания и т.д.`
- провести проверку содержимого заказа с использованием внутреннего ПО (LEOS);
- доставка PACK осуществляется в несколько этапов (при наличии количества более 2);
- Перед выходом из ТС проверить оборудование отсутствие крупных сумм ДС (СЕЙФ) в наличии;
- Выйти из машины, извлечь ТМЦ компании из кузова ТС;
- убедится, что запирающие устройства/сигнализация ТС активированы (ПРОВЕСТИ ФИЗИЧЕСКУЮ ПРОВЕРКУ);
- максимально коротким и безопасным маршрутом проследовать в адрес доставки;
- если доставка осуществляется в квартиру жилого дома, перед входом в подъезд ОСТАНОВИТЕСЬ, ПРИСЛУШАЙТЕСЬ. Если установлены посторонние шумы, присутствие людей, дождитесь попутчиков;
- будьте максимально бдительны и собраны в период доставки;
- при  контакте с клиентом внимательно осмотрите его/ее, помещение;

*- ВАЖНО: ПЕРЕДАВАТЬ ТОВАРЫ ТОЛЬКО УБЕДИВШИСЬ, ЧТО ТОВАР СООТВЕТСТВУЕТ ИЗОБРАЖЕНИЮ НА САЙТЕ;*

*- ВАЖНО: ПЕРЕДАВАТЬ ТОВАРЫ ПО 3 (ТРИ) ЕДИНИЦЫ ДЛЯ ПРИМЕРКИ ЗА РАЗ, ДОЖДАТЬСЯ ВОЗВРАТА, ПРОВЕРИТЬ ТОВАР И ВЫДАВАТЬ СЛЕДУЮЩИЕ ЕДИНИЦЫ;*

*-ВАЖНО: ПРОВЕРИТЬ СООТВЕТСТВИЕ ВСЕХ ЕДИНИЦ ТОВАРА ИЗОБРАЖЕНИЯМ после окончания примерки;*

- в случае наличного расчета *внимательно осмотреть все купюры*, переданные клиентом.
Если одна из купюр вызывает сомнение в подлинности, попросить клиента заменить ее.

*ЧТО ВАС ДОЛЖНО НАСТОРОЖИТЬ:
- доставка товара в малообжитые, труднодоступные места;
- получение уведомления от непосредственного руководителя/службы безопасности;
- изменение адреса/времени доставки клиентом;
- при проверке позиций заказа клиентом НЕ ПРИМЕНЕНА скидка;
- наличие высоко стоимостных позиций в заказе;
- ранее незнакомый клиент;     
- несоответствие заказанных позиций «социальному» статусу жилья и клиента;
- 1,2 этажи жилого сектора, офисные помещения с большой проходимостью, отдельно стоящие (заброшенные) жилые/промышленные строения, съемные квартиры, отсутствие признаков постоянного проживания/нахождения в помещении и т.д.
- нервозное состояние и поведение клиента;
- попытка произвести пересорт товара;
- попытка отвлечения внимания при выдаче, проверке товара, расчете.*"""
uk1 = """*1. Что такое сервис удаленной фискализации (удаленная касса)?*

Удаленная касса – это касса, физически установленная в ibox и подключенная через их приложение к
определенному сотруднику.
Торговому представителю больше не нужно получать, подключать и использовать мобильную кассу, бумажных
чеков и отчетов больше нет – есть только электронные чеки.
Клиент получает электронный чек в письме на адрес своей электронной почты, которую использовал при
регистрации аккаунта в сервисах Lamoda."""