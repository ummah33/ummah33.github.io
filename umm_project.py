Bismillahir_Rohmanir_Rohiym = "B.R.R."
print= Bismillahir_Rohmanir_Rohiym

import config
import telebot 
from telebot import types
from telebot.types import InputMediaPhoto

bot = telebot.TeleBot(config.TOKEN)

#STARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTART
#STARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTART
#STARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTART

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
    if call.data == '🇺🇿':
        markup = types.InlineKeyboardMarkup(row_width=2)
        # btn1 = types.InlineKeyboardButton("BEKTEMIR",callback_data ="BEKTEMIR")
        btn2 = types.InlineKeyboardButton("CHILONZOR",callback_data ="CHILONZOR")
        # btn3 = types.InlineKeyboardButton("MIROBOD",callback_data ="MIROBOD")
        # btn4 = types.InlineKeyboardButton("MIRZO ULUG'BEK",callback_data ="MIRZO ULUG'BEK")
        # btn5 = types.InlineKeyboardButton("OLMAZOR",callback_data ="OLMAZOR")
        # btn6 = types.InlineKeyboardButton("SERGELI",callback_data ="SERGELI")
        # btn7 = types.InlineKeyboardButton("SHAYXONTOHUR",callback_data ="SHAYXONTOHUR")
        # btn8 = types.InlineKeyboardButton("UCHTEPA",callback_data ="UCHTEPA")
        # btn9 = types.InlineKeyboardButton("YAKKASAROY",callback_data ="YAKKASAROY")
        # btn10 = types.InlineKeyboardButton("YASHNAOBOD",callback_data ="YASHNAOBOD")
        # btn11 = types.InlineKeyboardButton("YUNUSOBOD",callback_data ="YUNUSOBOD")
        # btn12 = types.InlineKeyboardButton("Yordam🆘",callback_data="yordam")
        markup.add(btn2,)#btn1,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id,text= "<b><ins>***   {0.first_name}   ***</ins>\n"
                                                    "_Xush kelibsiz_\n"
                                                    "Xozirda faqat shu tumandagi\n"
                                                    "mexmonxonalar bilan ishlamoqdamiz</b>"
                                                    .format(call.from_user),
                                                    reply_markup=markup, 
                                                    parse_mode="html")

#STARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTART
#STARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTART
#STARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTARTSTART

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

#CHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZOR
#CHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZOR
#CHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZOR

    if call.data == 'CHILONZOR':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("1️⃣ kishilik",callback_data ="chilonzor:1️⃣ kishilik")
        btn2 = types.InlineKeyboardButton("2️⃣ kishilik",callback_data ="chilonzor:2️⃣ kishilik")
        btn3 = types.InlineKeyboardButton("3️⃣ kishilik",callback_data ="chilonzor:3️⃣ kishilik")
        btn4 = types.InlineKeyboardButton("Lux",callback_data ="chilonzor:Lux")
        btn5 =types.InlineKeyboardButton("ortga↩️",callback_data="🇺🇿")
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id,text= "<b><ins>CHILONZOR-tumani</ins>\n\nXONA TURINI TANLANG!</b>",
                                                    reply_markup=markup, 
                                                    parse_mode="html")

    if call.data == 'chilonzor:1️⃣ kishilik':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("DIAMOND TASHKENT HOTEL", callback_data="DIAMOND TASHKENT HOTEL 1 KISHILIK")
        btn2 = types.InlineKeyboardButton("2-TEST HOTEL", callback_data="2:100-150")
        btn3 = types.InlineKeyboardButton("3-TEST HOTEL", callback_data="3:100-150")
        btn4 = types.InlineKeyboardButton("4-TEST HOTEL", callback_data="4:100-150")
        btn5 = types.InlineKeyboardButton("ortga↩️",callback_data="CHILONZOR")
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, text="<b><ins>CHILONZOR-tumani</ins>\n\n1 KISHILIK XONASI BOR MEXMON XONALAR\n\nKerakli Mexmonxonani tanlang tanlang!</b>",
                                                    reply_markup=markup, 
                                                    parse_mode="html")
    
    if call.data == "DIAMOND TASHKENT HOTEL 1 KISHILIK":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/DIAMOND_TASHKENT_HOTEL_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:1️⃣ kishilik")
        markup.add(btn2,btn3)
        p = open("D:\DIAMOND\single_room\DIAMOND_1.jpg","rb")
        b = open("D:\DIAMOND\single_room\DIAMOND_2.jpg","rb")
        c = open("D:\DIAMOND\single_room\DIAMOND_3.jpg","rb")
        d = open("D:\DIAMOND\single_room\DIAMOND_4.jpg","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p),InputMediaPhoto(b),InputMediaPhoto(c),InputMediaPhoto(d)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "<b>Xona xaqida ma'lumot!\n\nЦЕНА\nVatandoshlarimizga:</b>\n250 000 so'm\n\n<b>Mexmonlarimizga:</b>\n270 000 so'm\n<b>\n"
                                                                "SHARTLAR\n"
                                                                " <b>1.KIRISH-</b>"
                                                                " <ins>14:00.</ins>\n"
                                                                " <b>2.CHIQISH-</b>"
                                                                " <ins>12:00.</ins>\n"
                                                                "<b>Er-xotinlar ro'yxatga olish idorasi mavjud bo'lganda qabul qilinadi!</b>\n\n"
                                                                "Xizmatlar va qulayliklar:</b>\n\n"
        "✔️|Nonushta\n✔️|dush\n✔️|5 yoshgacha bo'lgan bolalar uchun turar joy va nonushta bepul \n✔️|sochiqlar\n✔️|televizor\n✔️|konditsioner\n✔️|hojatxona \n✔️|xususiy hammom\n✔️|kundalik xonani tozalash\n✔️|isitish tizimi\n✔️|kiyinish xonasi\n✔️|vanna yoki dush\n✔️|tekis ekranli televizor\n✔️|alohida kirish\n✔️|ovoz izolyatsiyasi\n✔️|derazadan ko'rinish\n✔️|shkaf\n✔️|kiyim ilgichi\n✔️|tualet qog'ozi\n✔️|tutqichli hojatxona\n✔️|axlat savatlari \n✔️|shampun\n✔️|sovun\n✔️|tutun sensori\n✔️|oyna", reply_markup=markup,parse_mode="html")
 
    if call.data == "2:100-150":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:1️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Ayni paytda muzokaralar olib borilmoqda", reply_markup=markup,parse_mode="html")

    if call.data == "3:100-150":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:1️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Ayni paytda muzokaralar olib borilmoqda", reply_markup=markup,parse_mode="html")
    
    if call.data == "4:100-150":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:1️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Ayni paytda muzokaralar olib borilmoqda", reply_markup=markup,parse_mode="html")

    if call.data == "chilonzor:2️⃣ kishilik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("DIAMOND TASHKENT HOTEL", callback_data="DIAMOND TASHKENT HOTEL 2 KISHILIK")
        btn2 = types.InlineKeyboardButton("2-TEST HOTEL", callback_data="2:150-200")
        btn3 = types.InlineKeyboardButton("3-TEST HOTEL", callback_data="3:150-200")
        btn4 = types.InlineKeyboardButton("4-TEST HOTEL", callback_data="4:150-200")
        btn5 = types.InlineKeyboardButton("ortga↩️",callback_data="CHILONZOR")
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, text="<b><ins>CHILONZOR-tumani</ins>\n\n2 KISHILIK XONASI BOR MEXMON XONALAR\n\nKerakli Mexmonxonani tanlang tanlang!</b>",
                                                    reply_markup=markup, 
                                                    parse_mode="html")
                                                        
    if call.data == "DIAMOND TASHKENT HOTEL 2 KISHILIK":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/DIAMOND_TASHKENT_HOTEL_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:2️⃣ kishilik")
        markup.add(btn2,btn3)
        p = open("D:\DIAMOND\standart_twin\DIAMOND_1.jpg","rb")
        b = open("D:\DIAMOND\standart_twin\DIAMOND_2.jpg","rb")
        c = open("D:\DIAMOND\standart_twin\DIAMOND_3.jpg","rb")
        d = open("D:\DIAMOND\standart_twin\DIAMOND_4.jpg","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p),InputMediaPhoto(b),InputMediaPhoto(c),InputMediaPhoto(d)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "<b>Xona xaqida ma'lumot!\n\nЦЕНА\nVatandoshlarimizga:</b>\n350 000 so'm\n\n<b>Mexmonlarimizga:</b>\n400 000 so'm\n<b>\n"
                                                                "SHARTLAR\n"
                                                                " <b>1.KIRISH-</b>"
                                                                " <ins>14:00.</ins>\n"
                                                                " <b>2.CHIQISH-</b>"
                                                                " <ins>12:00.</ins>\n"
                                                                "<b>Er-xotinlar ro'yxatga olish idorasi mavjud bo'lganda qabul qilinadi!</b>\n\n"
                                                                "Xizmatlar va qulayliklar:</b>\n\n"
        "✔️|Nonushta\n✔️|dush\n✔️|5 yoshgacha bo'lgan bolalar uchun turar joy va nonushta bepul \n✔️|sochiqlar\n✔️|televizor\n✔️|konditsioner\n✔️|hojatxona \n✔️|xususiy hammom\n✔️|kundalik xonani tozalash\n✔️|isitish tizimi\n✔️|kiyinish xonasi\n✔️|vanna yoki dush\n✔️|tekis ekranli televizor\n✔️|alohida kirish\n✔️|ovoz izolyatsiyasi\n✔️|derazadan ko'rinish\n✔️|shkaf\n✔️|kiyim ilgichi\n✔️|tualet qog'ozi\n✔️|tutqichli hojatxona\n✔️|axlat savatlari \n✔️|shampun\n✔️|sovun\n✔️|tutun sensori\n✔️|oyna", reply_markup=markup,parse_mode="html")
 
    if call.data == "2:150-200":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:2️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Ayni paytda muzokaralar olib borilmoqda", reply_markup=markup,parse_mode="html")

    if call.data == "3:150-200":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:2️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Ayni paytda muzokaralar olib borilmoqda", reply_markup=markup,parse_mode="html")    
    
    if call.data == "4:150-200":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:2️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Ayni paytda muzokaralar olib borilmoqda", reply_markup=markup,parse_mode="html")
  

    if call.data == "chilonzor:3️⃣ kishilik":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("DIAMOND TASHKENT HOTEL", callback_data="DIAMOND TASHKENT HOTEL 3 KISHILIK")
        btn2 = types.InlineKeyboardButton("2-TEST HOTEL", callback_data="2:200-300")
        btn3 = types.InlineKeyboardButton("3-TEST HOTEL", callback_data="3:200-300")
        btn4 = types.InlineKeyboardButton("4-TEST HOTEL", callback_data="4:200-300")
        btn5 = types.InlineKeyboardButton("ortga↩️",callback_data="CHILONZOR")
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, text="<b><ins>CHILONZOR-tumani</ins>\n\n3 KISHILIK XONASI BOR MEXMON XONALAR\n\nKerakli Mexmonxonani tanlang tanlang!</b>",
                                                    reply_markup=markup, 
                                                    parse_mode="html")
                                                        
    if call.data == "DIAMOND TASHKENT HOTEL 3 KISHILIK":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/DIAMOND_TASHKENT_HOTEL_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:3️⃣ kishilik")
        markup.add(btn2,btn3)
        p = open("D:\DIAMOND\Triple_standart\DIAMOND_1.jpg","rb")
        b = open("D:\DIAMOND\Triple_standart\DIAMOND_3.jpg","rb")
        c = open("D:\DIAMOND\Triple_standart\DIAMOND_4.jpg","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p),InputMediaPhoto(b),InputMediaPhoto(c)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "<b>Xona xaqida ma'lumot!\n\nЦЕНА\nVatandoshlarimizga:</b>\n400 000 so'm\n\n<b>Mexmonlarimizga:</b>\n450 000 so'm\n<b>\n"
                                                                "SHARTLAR\n"
                                                                " <b>1.KIRISH-</b>"
                                                                " <ins>14:00.</ins>\n"
                                                                " <b>2.CHIQISH-</b>"
                                                                " <ins>12:00.</ins>\n"
                                                                "<b>Er-xotinlar ro'yxatga olish idorasi mavjud bo'lganda qabul qilinadi!</b>\n\n"
                                                                "Xizmatlar va qulayliklar:</b>\n\n"
        "✔️|Nonushta\n✔️|dush\n✔️|5 yoshgacha bo'lgan bolalar uchun turar joy va nonushta bepul \n✔️|sochiqlar\n✔️|televizor\n✔️|konditsioner\n✔️|hojatxona \n✔️|xususiy hammom\n✔️|kundalik xonani tozalash\n✔️|isitish tizimi\n✔️|kiyinish xonasi\n✔️|vanna yoki dush\n✔️|tekis ekranli televizor\n✔️|alohida kirish\n✔️|ovoz izolyatsiyasi\n✔️|derazadan ko'rinish\n✔️|shkaf\n✔️|kiyim ilgichi\n✔️|tualet qog'ozi\n✔️|tutqichli hojatxona\n✔️|axlat savatlari \n✔️|shampun\n✔️|sovun\n✔️|tutun sensori\n✔️|oyna", reply_markup=markup,parse_mode="html")
 
    if call.data == "2:200-300":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:3️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Ayni paytda muzokaralar olib borilmoqda", reply_markup=markup,parse_mode="html")

    if call.data == "3:200-300":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:3️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Ayni paytda muzokaralar olib borilmoqda", reply_markup=markup,parse_mode="html")
    
    if call.data == "4:200-300":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:3️⃣ kishilik")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Ayni paytda muzokaralar olib borilmoqda", reply_markup=markup,parse_mode="html")

#************************************************************************************************************

    if call.data =='chilonzor:Lux':
        markup =types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("DIAMOND TASHKENT HOTEL", callback_data="DIAMOND TASHKENT HOTEL LUX XONA")
        btn2 = types.InlineKeyboardButton("2-TEST HOTEL", callback_data="chilonzor:600-650 ming")
        btn3 = types.InlineKeyboardButton("3-TEST HOTEL", callback_data="chilonzor:700-750 ming")
        btn4 = types.InlineKeyboardButton("4-TEST HOTEL", callback_data="chilonzor:750-800 ming")
        btn5 =types.InlineKeyboardButton("ortga↩️",callback_data="CHILONZOR")
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, text="<b><ins>CHILONZOR-tumani</ins>\n\nLUX XONASI BOR MEXMON XONALAR\n\nKerakli Mexmonxonani tanlang!</b>",
                                                    reply_markup=markup, 
                                                    parse_mode="html")
    
    if call.data == "DIAMOND TASHKENT HOTEL LUX XONA":
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/DIAMOND_TASHKENT_HOTEL_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:Lux")
        markup.add(btn2,btn3)
        p = open("D:\DIAMOND\lux\DIAMOND_1.jpg","rb")
        b = open("D:\DIAMOND\lux\DIAMOND_2.jpg","rb")
        c = open("D:\DIAMOND\lux\DIAMOND_3.jpg","rb")
        d = open("D:\DIAMOND\lux\DIAMOND_4.jpg","rb")
        e = open("D:\DIAMOND\lux\DIAMOND_5.jpg","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p),InputMediaPhoto(b),InputMediaPhoto(c),InputMediaPhoto(d),InputMediaPhoto(e)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "<b>Xona xaqida ma'lumot!\n\nЦЕНА\nVatandoshlarimizga:</b>\n550 000 so'm\n\n<b>Mexmonlarimizga:</b>\n600 000 so'm\n<b>\n"
                                                                "SHARTLAR\n"
                                                                " <b>1.KIRISH-</b>"
                                                                " <ins>14:00.</ins>\n"
                                                                " <b>2.CHIQISH-</b>"
                                                                " <ins>12:00.</ins>\n"
                                                                "<b>Er-xotinlar ro'yxatga olish idorasi mavjud bo'lganda qabul qilinadi!</b>\n\n"
                                                                "Xizmatlar va qulayliklar:</b>\n\n"
        "✔️|Nonushta\n✔️|dush\n✔️|5 yoshgacha bo'lgan bolalar uchun turar joy va nonushta bepul \n✔️|sochiqlar\n✔️|televizor\n✔️|konditsioner\n✔️|hojatxona \n✔️|xususiy hammom\n✔️|kundalik xonani tozalash\n✔️|isitish tizimi\n✔️|kiyinish xonasi\n✔️|vanna yoki dush\n✔️|tekis ekranli televizor\n✔️|alohida kirish\n✔️|ovoz izolyatsiyasi\n✔️|derazadan ko'rinish\n✔️|shkaf\n✔️|kiyim ilgichi\n✔️|tualet qog'ozi\n✔️|tutqichli hojatxona\n✔️|axlat savatlari \n✔️|shampun\n✔️|sovun\n✔️|tutun sensori\n✔️|oyna", reply_markup=markup,parse_mode="html")
 
    if call.data == "chilonzor:600-650 ming":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:Lux")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Ayni paytda muzokaralar olib borilmoqda", reply_markup=markup,parse_mode="html")

    if call.data == "chilonzor:700-750 ming":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:Lux")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Ayni paytda muzokaralar olib borilmoqda", reply_markup=markup,parse_mode="html")
    
    if call.data == "chilonzor:750-800 ming":
        markup = types.InlineKeyboardMarkup(row_width=1)
        # btn3 = types.InlineKeyboardButton("Band qilish-1️⃣",url="https://t.me/HALAL_Food1_bot")
        btn2 = types.InlineKeyboardButton("ortga↩️",callback_data="chilonzor:Lux")
        markup.add(btn2)
        p = open("D:\личные проекты — копия\logo.png","rb")
        bot.send_media_group(call.message.chat.id, [InputMediaPhoto(p)])
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Ayni paytda muzokaralar olib borilmoqda", reply_markup=markup,parse_mode="html")


#CHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZOR
#CHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZOR
#CHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZORCHILONZOR

bot.remove_webhook()
bot.polling()