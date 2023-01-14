Bismillahir_Rohmanir_Rohiym = "B.R.R."
print= Bismillahir_Rohmanir_Rohiym

import config
import telebot 
from telebot import types
from telebot.types import InputMediaPhoto

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=["text"])
def start(message):
    if (message.text == '/start'):
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("🇺🇿",callback_data ="🇺🇿")
        btn2 = types.InlineKeyboardButton("🇷🇺",callback_data ="🇷🇺")
        markup.add(btn1,btn2)
        bot.send_message(message.chat.id, text="<b>Assalamu Alaykum\n"
                                    "Tilni tanlang!\n"
                                    "🇺🇿\n\n"
                                    "Здравствуйте\n"
                                    "Выберите язык!</b>\n"
                                    "🇷🇺",
                                    reply_markup=markup,
                                    parse_mode="html")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == '🇷🇺' or call.data == 'Выбор района!':
        markup = types.InlineKeyboardMarkup(row_width=2)
        # btn1 = types.InlineKeyboardButton("БЕКТЕМИР",callback_data ="БЕКТЕМИР")
        btn2 = types.InlineKeyboardButton("ЧИЛАНЗАР",callback_data ="ЧИЛАНЗАР")
        # btn3 = types.InlineKeyboardButton("МИРАБАД",callback_data ="МИРАБАД")
        # btn4 = types.InlineKeyboardButton("МИРЗО-УЛУГБЕК",callback_data ="МИРЗО-УЛУГБЕК")
        # btn5 = types.InlineKeyboardButton("АЛМАЗАР",callback_data ="АЛМАЗАР")
        # btn6 = types.InlineKeyboardButton("Сергели",callback_data ="СЕРГЕЛИ")
        # btn7 = types.InlineKeyboardButton("ШАЙХАНТАХУР",callback_data ="ШАЙХАНТАХУР")
        # btn8 = types.InlineKeyboardButton("УЧТЕПА",callback_data ="УЧТЕПА")
        # btn9 = types.InlineKeyboardButton("ЯККАСАРАЙ",callback_data ="ЯККАСАРАЙ")
        # btn10 = types.InlineKeyboardButton("ЯШНАБАД",callback_data ="ЯШНАБАД")
        # btn11 = types.InlineKeyboardButton("ЮНУСАБАД",callback_data ="ЮНУСАБАД")
        # btn12 = types.InlineKeyboardButton("ПОМОЩЬ🆘",callback_data="ПОМОЩЬ")
        markup.add(btn2,)#btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id,text= "<b><ins>***              {0.first_name}              ***</ins>\n"
                                                    "     _ДОБРО ПОЖАЛОВАТЬ_\n"
                                                    "ИЗ КАКОГО РАЙОНА ТАШКЕНТА ВАМ НУЖНА ГОСТИНИЦА</b>"
                                                    .format(call.from_user),
                                                    reply_markup=markup,  
                                                    parse_mode="html")

#CHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZOR
#CHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZOR
#CHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZOR

    if call.data == 'ЧИЛАНЗАР':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("1️⃣-МЕСТНЫЙ",callback_data ="chilonzor:1️⃣ kishilik")
        btn2 = types.InlineKeyboardButton("2️⃣ух-МЕСТНЫЙ",callback_data ="chilonzor:2️⃣ kishilik")
        btn3 = types.InlineKeyboardButton("3️⃣ех-МЕСТНЫЙ",callback_data ="chilonzor:3️⃣ kishilik")
        btn4 = types.InlineKeyboardButton("⚜️Lux",callback_data ="chilonzor:Lux")
        btn5 =types.InlineKeyboardButton("назад↩️",callback_data="🇷🇺")
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id,text= "<b><ins>    ЧИЛАНЗАРСКИЙ-РАЙОН</ins>\n\nВЫБЕРИТЕ ТИП КОМНАТЫ!</b>",
                                                    reply_markup=markup, 
                                                    parse_mode="html")

    if call.data == 'chilonzor:1️⃣ kishilik':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("DIAMOND TASHKENT HOTEL", callback_data="DIAMOND TASHKENT HOTEL 1 KISHILIK")
        btn2 = types.InlineKeyboardButton("2-ТЕСТ ГОСТИНИЦА", callback_data="2:100-150")
        btn3 = types.InlineKeyboardButton("3-ТЕСТ ГОСТИНИЦА", callback_data="3:100-150")
        btn4 = types.InlineKeyboardButton("4-ТЕСТ ГОСТИНИЦА", callback_data="4:100-150")
        btn5 = types.InlineKeyboardButton("назад↩️",callback_data="ЧИЛАНЗАР")
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, text="<b><ins>    ЧИЛАНЗАРСКИЙ-РАЙОН</ins>\n\nГОСТЕВЫЕ НОМЕРА С 1-МЕСТНОЙ КОМНАТОЙ\n\nВыберите желаемый отель!</b>",
                                                    reply_markup=markup, 
                                                    parse_mode="html")
    
    if call.data == "DIAMOND TASHKENT HOTEL 1 KISHILIK":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/DIAMOND_TASHKENT_HOTEL_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:1️⃣ kishilik")
        markup.add(btn2,btn3)
        p = open("D:\DIAMOND\single_room\DIAMOND_1.jpg","rb")
        b = open("D:\DIAMOND\single_room\DIAMOND_2.jpg","rb")
        c = open("D:\DIAMOND\single_room\DIAMOND_3.jpg","rb")
        d = open("D:\DIAMOND\single_room\DIAMOND_4.jpg","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p),InputMediaPhoto(b),InputMediaPhoto(c),InputMediaPhoto(d)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "<b>Информация о номере!\n\nЦЕНА\nРезидентам:</b>\n250 000 сум\n\n<b>Не Резидентам:</b>\n270 000 сум\n<b>\n"
                                                                "УСЛОВИЯ\n"
                                                                " <b>1.ЗАЕЗД-</b>"
                                                                " <ins>14:00.</ins>\n"
                                                                " <b>2.ВЫЕЗД-</b>"
                                                                " <ins>12:00.</ins>\n"
                                                                "<b>Семейные пары впускается при наличии ЗАГС!</b>\n\n"
                                                                "Услуги и удобства:</b>\n\n"
        "✔️|Завтрак\n✔️|Душ\n✔️|Детям до 5 лет проживание и завтрак бесплатно\n✔️|Полотенца\n✔️|Телевизор\n✔️|Кондиционер\n✔️|Туалет\n✔️|Собственная ванная комната\n✔️|Ежедневная уборка номера\n✔️|Отопление\n✔️|Гардеробная\n✔️|Ванна или душ\n✔️|Телевизор с плоским экраном\n✔️|Отдельный вход\n✔️|Звукоизоляция\n✔️|Вид из окна\n✔️|Шкаф и гардероб\n✔️|Вешалка для одежды\n✔️|Туалетная бумага\n✔️|Туалет с поручнями\n✔️|Корзины для мусора\n✔️|Шампунь\n✔️|Мыло\n✔️|Датчик дыма\n✔️|Окно", reply_markup=markup,parse_mode="html")
 
    if call.data == "2:100-150":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:1️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "В данное время у нас идут переговары", reply_markup=markup,parse_mode="html")

    if call.data == "3:100-150":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:1️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "В данное время у нас идут переговары", reply_markup=markup,parse_mode="html")
    
    if call.data == "4:100-150":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:1️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "В данное время у нас идут переговары", reply_markup=markup,parse_mode="html")

    if call.data == "chilonzor:2️⃣ kishilik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("DIAMOND TASHKENT HOTEL", callback_data="DIAMOND TASHKENT HOTEL 2 KISHILIK")
        btn2 = types.InlineKeyboardButton("2-ТЕСТ ОТЕЛЬ", callback_data="2:150-200")
        btn3 = types.InlineKeyboardButton("3-ТЕСТ ОТЕЛЬ", callback_data="3:150-200")
        btn4 = types.InlineKeyboardButton("4-ТЕСТ ОТЕЛЬ", callback_data="4:150-200")
        btn5 = types.InlineKeyboardButton("назад↩️",callback_data="CHILONZOR")
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, text="<b><ins>    ЧИЛАНЗАРСКИЙ-РАЙОН</ins>\n\nГОСТЕВЫЕ НОМЕРА С 2ух-МЕСТНОЙ КОМНАТОЙ\n\nВыберите желаемый отель!</b>",
                                                    reply_markup=markup, 
                                                    parse_mode="html")
                                                        
    if call.data == "DIAMOND TASHKENT HOTEL 2 KISHILIK":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/DIAMOND_TASHKENT_HOTEL_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:2️⃣ kishilik")
        markup.add(btn2,btn3)
        p = open("D:\DIAMOND\standart_twin\DIAMOND_1.jpg","rb")
        b = open("D:\DIAMOND\standart_twin\DIAMOND_2.jpg","rb")
        c = open("D:\DIAMOND\standart_twin\DIAMOND_3.jpg","rb")
        d = open("D:\DIAMOND\standart_twin\DIAMOND_4.jpg","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p),InputMediaPhoto(b),InputMediaPhoto(c),InputMediaPhoto(d)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "<b>Информация о номере!\n\nЦЕНА\nРезидентам:</b>\n350 000 сум\n\n<b>Не Резидентам:</b>\n400 000 сум\n<b>\n"
                                                                "УСЛОВИЯ\n"
                                                                " <b>1.ЗАЕЗД-</b>"
                                                                " <ins>14:00.</ins>\n"
                                                                " <b>2.ВЫЕЗД-</b>"
                                                                " <ins>12:00.</ins>\n"
                                                                "<b>Семейные пары впускается при наличии ЗАГС!</b>\n\n"
                                                                "Услуги и удобства:</b>\n\n"
        "✔️|Завтрак\n✔️|Душ\n✔️|Детям до 5 лет проживание и завтрак бесплатно\n✔️|Полотенца\n✔️|Телевизор\n✔️|Кондиционер\n✔️|Туалет\n✔️|Собственная ванная комната\n✔️|Ежедневная уборка номера\n✔️|Отопление\n✔️|Гардеробная\n✔️|Ванна или душ\n✔️|Телевизор с плоским экраном\n✔️|Отдельный вход\n✔️|Звукоизоляция\n✔️|Вид из окна\n✔️|Шкаф и гардероб\n✔️|Вешалка для одежды\n✔️|Туалетная бумага\n✔️|Туалет с поручнями\n✔️|Корзины для мусора\n✔️|Шампунь\n✔️|Мыло\n✔️|Датчик дыма\n✔️|Окно", reply_markup=markup,parse_mode="html")
 
    if call.data == "2:150-200":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:2️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "В данное время у нас идут переговары", reply_markup=markup,parse_mode="html")

    if call.data == "3:150-200":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:2️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "В данное время у нас идут переговары", reply_markup=markup,parse_mode="html")    
    
    if call.data == "4:150-200":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:2️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "В данное время у нас идут переговары", reply_markup=markup,parse_mode="html")
  

    if call.data == "chilonzor:3️⃣ kishilik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("DIAMOND TASHKENT HOTEL", callback_data="DIAMOND TASHKENT HOTEL 3 KISHILIK")
        btn2 = types.InlineKeyboardButton("2-ТЕСТ ОТЕЛЬ", callback_data="2:200-300")
        btn3 = types.InlineKeyboardButton("3-ТЕСТ ОТЕЛЬ", callback_data="3:200-300")
        btn4 = types.InlineKeyboardButton("4-ТЕСТ ОТЕЛЬ", callback_data="4:200-300")
        btn5 = types.InlineKeyboardButton("назад↩️",callback_data="ЧИЛАНЗАР")
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, text="<b><ins>    ЧИЛАНЗАРСКИЙ-РАЙОН</ins>\n\nГОСТЕВЫЕ НОМЕРА С 3ех-МЕСТНОЙ КОМНАТОЙ\n\nВыберите желаемый отель!</b>",
                                                    reply_markup=markup, 
                                                    parse_mode="html")
                                                        
    if call.data == "DIAMOND TASHKENT HOTEL 3 KISHILIK":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/DIAMOND_TASHKENT_HOTEL_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:3️⃣ kishilik")
        markup.add(btn2,btn3)
        p = open("D:\DIAMOND\Triple_standart\DIAMOND_1.jpg","rb")
        b = open("D:\DIAMOND\Triple_standart\DIAMOND_3.jpg","rb")
        c = open("D:\DIAMOND\Triple_standart\DIAMOND_4.jpg","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p),InputMediaPhoto(b),InputMediaPhoto(c)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "<b>Информация о номере!\n\nЦЕНА\nРезидентам:</b>\n400 000 сум\n\n<b>Не Резидентам:</b>\n450 000 сум\n<b>\n"
                                                                "УСЛОВИЯ\n"
                                                                " <b>1.ЗАЕЗД-</b>"
                                                                " <ins>14:00.</ins>\n"
                                                                " <b>2.ВЫЕЗД-</b>"
                                                                " <ins>12:00.</ins>\n"
                                                                "<b>Семейные пары впускается при наличии ЗАГС!</b>\n\n"
                                                                "Услуги и удобства:</b>\n\n"
        "✔️|Завтрак\n✔️|Душ\n✔️|Детям до 5 лет проживание и завтрак бесплатно\n✔️|Полотенца\n✔️|Телевизор\n✔️|Кондиционер\n✔️|Туалет\n✔️|Собственная ванная комната\n✔️|Ежедневная уборка номера\n✔️|Отопление\n✔️|Гардеробная\n✔️|Ванна или душ\n✔️|Телевизор с плоским экраном\n✔️|Отдельный вход\n✔️|Звукоизоляция\n✔️|Вид из окна\n✔️|Шкаф и гардероб\n✔️|Вешалка для одежды\n✔️|Туалетная бумага\n✔️|Туалет с поручнями\n✔️|Корзины для мусора\n✔️|Шампунь\n✔️|Мыло\n✔️|Датчик дыма\n✔️|Окно", reply_markup=markup,parse_mode="html")
 
    if call.data == "2:200-300":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:3️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "В данное время у нас идут переговары", reply_markup=markup,parse_mode="html")

    if call.data == "3:200-300":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:3️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "В данное время у нас идут переговары", reply_markup=markup,parse_mode="html")
    
    if call.data == "4:200-300":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:3️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "В данное время у нас идут переговары", reply_markup=markup,parse_mode="html")

#************************************************************************************************************

    if call.data =='chilonzor:Lux':
        markup =types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("DIAMOND TASHKENT HOTEL", callback_data="DIAMOND TASHKENT HOTEL LUX XONA")
        btn2 = types.InlineKeyboardButton("2-ТЕСТ ОТЕЛЬ",callback_data="chilonzor:600-650 ming")
        btn3 = types.InlineKeyboardButton("3-ТЕСТ ОТЕЛЬ", callback_data="chilonzor:700-750 ming")
        btn4 = types.InlineKeyboardButton("4-ТЕСТ ОТЕЛЬ", callback_data="chilonzor:750-800 ming")
        btn5 =types.InlineKeyboardButton("назад↩️",callback_data="ЧИЛАНЗАР")
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, text="<b><ins>    ЧИЛАНЗАРСКИЙ-РАЙОН</ins>\n\nГОСТЕВЫЕ НОМЕРА С ЛЮКС КОМНАТОЙ\n\nВыберите желаемый отель!</b>",
                                                    reply_markup=markup, 
                                                    parse_mode="html")
    
    if call.data == "DIAMOND TASHKENT HOTEL LUX XONA":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/DIAMOND_TASHKENT_HOTEL_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:Lux")
        markup.add(btn2,btn3)
        p = open("D:\DIAMOND\lux\DIAMOND_1.jpg","rb")
        b = open("D:\DIAMOND\lux\DIAMOND_2.jpg","rb")
        c = open("D:\DIAMOND\lux\DIAMOND_3.jpg","rb")
        d = open("D:\DIAMOND\lux\DIAMOND_4.jpg","rb")
        e = open("D:\DIAMOND\lux\DIAMOND_5.jpg","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p),InputMediaPhoto(b),InputMediaPhoto(c),InputMediaPhoto(d),InputMediaPhoto(e)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "<b>Информация о номере!\n\nЦЕНА\nРезидентам:</b>\n550 000 сум\n\n<b>Не Резидентам:</b>\n600 000 сум\n<b>\n"
                                                                "УСЛОВИЯ\n"
                                                                " <b>1.ЗАЕЗД-</b>"
                                                                " <ins>14:00.</ins>\n"
                                                                " <b>2.ВЫЕЗД-</b>"
                                                                " <ins>12:00.</ins>\n"
                                                                "<b>Семейные пары впускается при наличии ЗАГС!</b>\n\n"
                                                                "Услуги и удобства:</b>\n\n"
        "✔️|Завтрак\n✔️|Душ\n✔️|Детям до 5 лет проживание и завтрак бесплатно\n✔️|Полотенца\n✔️|Телевизор\n✔️|Кондиционер\n✔️|Туалет\n✔️|Собственная ванная комната\n✔️|Ежедневная уборка номера\n✔️|Отопление\n✔️|Гардеробная\n✔️|Ванна или душ\n✔️|Телевизор с плоским экраном\n✔️|Отдельный вход\n✔️|Звукоизоляция\n✔️|Вид из окна\n✔️|Шкаф и гардероб\n✔️|Вешалка для одежды\n✔️|Туалетная бумага\n✔️|Туалет с поручнями\n✔️|Корзины для мусора\n✔️|Шампунь\n✔️|Мыло\n✔️|Датчик дыма\n✔️|Окно", reply_markup=markup,parse_mode="html")
 
    if call.data == "chilonzor:600-650 ming":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:Lux")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "В данное время у нас идут переговары", reply_markup=markup,parse_mode="html")

    if call.data == "chilonzor:700-750 ming":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:Lux")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "В данное время у нас идут переговары", reply_markup=markup,parse_mode="html")
    
    if call.data == "chilonzor:750-800 ming":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("БРОНИРОВАНИЕ-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("назад↩️",callback_data="chilonzor:Lux")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "В данное время у нас идут переговары", reply_markup=markup,parse_mode="html")


#CHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZOR
#CHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZOR
#CHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZOR

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

bot.remove_webhook()
bot.polling()