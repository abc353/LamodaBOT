token = "1062778180:AAHeLcSKVCAy23PKnRhMRy5Y3HR2bs3xblg"
vpn = 'CgACAgIAAxkBAAIH1GFJK3uBEM69kSfWNxCinKG2XC6JAAINDgAClexRSgOcbRmSsJyZIAQ'
bps = 'CgACAgIAAxkBAAILP2FOWTxLvFr9piR4GgaP9EUt55YOAALOEAAC8dhwSumWIL4WwL0yIQQ'
perenos = """1 - Выясняем причину
2 - Предлагаем доставку заказа в другой интервал сегодня же
3 - Предлагаем доставку по другому адресу, главное чтобы клиент принял сегодня `адрес согласовываем с супервайзером`
3.1 - Важно показать гибкость и лояльность компании, используя каждый раз все 3 пункта.
`так вы точно поймете, нужен ли клиенту заказ`"""
otmena = """1 - Отмена по просьбе клиента `крайне желательно подтверждение отмены по рабочему телефону в звонке`
2 - У заказа последняя-3я попытка доставки `смотрим через статус недозвон или в маршрутнике`
2.1 - У заказа кончаются дни хранения на складе. Всего 5 дней
`если у вас 3 дня хранения, то перенести можно на завтра или послезавтра`
3 - Фактический адрес доставки не входит в зону Южного склада. `уточняем у супервайзера`
*Только оформление нового заказа с корректным адресом. Перенос невозможен*"""
contact = """*Call Центр* +74995004959
*Дежурный СВ* +79160558030
*Дежурный механик* +79150110787
*Дежурный кассир* +79175805523
*Паркоматика* +78003015748
*Мокка* +78007077236
*iboxPro* +74955055045 +78003334526
*СБ* +79999991489"""
promokod = """Для получения корпоративных promo-кодов зарегистрируйся на lamoda.ru, используя логин *iBox*
`номер телефона должен совпадать с указанным в отделе кадров`"""
opozdanie = """Очень важно позвонить клиенту до окончания интервала `за 30-60мин` и проинформировать о возможном опоздании, например:

_Анна Петровна, LMexp, ТП Александр, чуть задерживаюсь к Вам. Было бы Вам удобно принять заказ позже 12?_ `интервал до 12`

_Анна Петровна, меня зовут Александр, доставляю Ваш заказ от Lamoda, возможно не успею в интервал до 12. Могли бы Вы пойти на встречу и принять заказ в удобное для Вас время позже?_"""
bezcheka = """Клиент оплатил, а заказ остался на карте. Что делать?
Проверяем успешность платежа. Успешен? `уходим от клиента` Выключаем POS в настройках Lmexp
Отмечаем в точности те же позиции и тот же метод оплаты - закрываем заказ.
Включаем POS в настройках Lmexp"""
oplata = """Заходим в *iBox* история платежей. Тянем вниз - обновляется список платежей. `должно быть соединение с интернетом`
Самым первым будет ваш крайний заказ. Открываем его, слева внизу ищем *Платеж успешен*
Если платежа нет, или он не успешен - *Деньги Не Поступили*
Проводим оплату заново!"""
#- Обновляем все заказы, заходим в настройки телефона.
#`меню - приложения - Lmexpess mobile - Память - Очистить кэш и данные`
#Заходим заново Lmexpess mobile, в заказах списком находим клиента, жмем корзинку
anyconnect = """Добавляем сертификат"""
elchek = """*А где бумажный чек?*

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