Bismillahir_Rohmanir_Rohiym = "B.R.R."
print= Bismillahir_Rohmanir_Rohiym

import telebot 
from telebot import types
from telebot.types import InputMediaPhoto
import config

user_dict = {}
user_chats = 0

class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.languages = None
        self.sex = None
        keys = ['age', 'languages', 'git_acc']
        for key in keys:
            self.key = None

bot = telebot.TeleBot(config.token_diamond)

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
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("1️⃣ KISHILIK",callback_data ="ONE")
        btn2 = types.InlineKeyboardButton("2️⃣ KISHILIK",callback_data ="TWO")
        btn3 = types.InlineKeyboardButton("3️⃣ KISHILIK",callback_data ="THREE")
        btn4 = types.InlineKeyboardButton("⚜️ LUX",callback_data ="LUX")
        btn5 =types.InlineKeyboardButton("🗺 yandex.maps!", url="https://yandex.uz/maps/-/CCUrr-cpLC")
        markup.add(btn1,btn2,btn3,btn4,btn5)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id,text= "<b><ins>***   {0.first_name}   ***</ins>\n"
                                                    "Qaysi xona turini tanladingiz?</b>"
                                                    .format(call.from_user),
                                                    reply_markup=markup, 
                                                    parse_mode="html")
  
    if call.data =='ONE':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('ДА',callback_data="YES-1")
        btn2 = types.InlineKeyboardButton('НЕТ',callback_data='🇺🇿')            
        markup.add(btn1,btn2)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Вы точно хотите бронировать НОМЕР ?", reply_markup=markup,parse_mode='Markdown')
    if call.data == "YES-1":
                chat_id =call.message.chat.id
                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                msg_1 = bot.send_message(chat_id, "Отправьте ваш Ф.И.О.")
                bot.register_next_step_handler(msg_1, process_name_step_1)
#payment1#payment1#payment1#payment1#payment1#payment1#payment1
#payment1#payment1#payment1#payment1#payment1#payment1#payment1
    if call.data == 'yes_1':
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Информация от бота: ", reply_markup=None)
          bot.send_message(call.message.chat.id,call.from_user.first_name + ' отправил(а) инвойс клиенту:' + '(' + call.from_user.username +')')
          p = open(("D:\личные проекты — копия\logo.png"),"rb")
          bot.send_photo(user_chats, p)
          bot.send_invoice(user_chats,   #chat_id
                  'БРОНИРОВАНИЕ НОМЕРА!', #title
                  'Нажмите на кнопку заплатить', #description
                  '!_!', #invoice_payload
                  config.provider_token_click, #provider_token
                  'UZS', #currency
                  config.prices_1, #prices
                  is_flexible=False,
                  start_parameter='hotel')
#payment2#payment2#payment2#payment2#payment2#payment2#payment2
#payment2#payment2#payment2#payment2#payment2#payment2#payment2
    if call.data == 'yes_2':
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Информация от бота: ", reply_markup=None)
          bot.send_message(call.message.chat.id,call.from_user.first_name + ' отправил(а) инвойс клиенту:' + '(' + call.from_user.username +')')
          p = open(("D:\личные проекты — копия\logo.png"),"rb")
          bot.send_photo(user_chats, p)
          bot.send_invoice(user_chats,   #chat_id
                  'БРОНИРОВАНИЕ НОМЕРА!', #title
                  'Нажмите на кнопку заплатить', #description
                  '!_!', #invoice_payload
                  config.provider_token_click, #provider_token
                  'UZS', #currency
                  config.prices_2, #prices
                  is_flexible=False,
                  start_parameter='hotel')
#payment3#payment3#payment3#payment3#payment3#payment3#payment3
#payment3#payment3#payment3#payment3#payment3#payment3#payment3
    if call.data == 'yes_3':
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Информация от бота: ", reply_markup=None)
          bot.send_message(call.message.chat.id,call.from_user.first_name + ' отправил(а) инвойс клиенту:' + '(' + call.from_user.username +')')
          p = open(("D:\личные проекты — копия\logo.png"),"rb")
          bot.send_photo(user_chats, p)
          bot.send_invoice(user_chats,   #chat_id
                  'БРОНИРОВАНИЕ НОМЕРА!', #title
                  'Нажмите на кнопку заплатить', #description
                  '!_!', #invoice_payload
                  config.provider_token_click, #provider_token
                  'UZS', #currency
                  config.prices_4, #prices
                  is_flexible=False,
                  start_parameter='hotel')
#payment4#payment4#payment4#payment4#payment4#payment4#payment4
#payment4#payment4#payment4#payment4#payment4#payment4#payment4
    if call.data == 'yes_4':
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Информация от бота: ", reply_markup=None)
          bot.send_message(call.message.chat.id,call.from_user.first_name + ' отправил(а) инвойс клиенту:' + '(' + call.from_user.username +')')
          p = open(("D:\личные проекты — копия\logo.png"),"rb")
          bot.send_photo(user_chats, p)
          bot.send_invoice(user_chats,   #chat_id
                  'БРОНИРОВАНИЕ НОМЕРА!', #title
                  'Нажмите на кнопку заплатить', #description
                  '!_!', #invoice_payload
                  config.provider_token_click, #provider_token
                  'UZS', #currency
                  config.prices_5, #prices
                  is_flexible=False,
                  start_parameter='hotel')
    if call.data == "no":
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Информация от бота: ", reply_markup=None)
          bot.send_message(call.message.chat.id,call.from_user.first_name + ' не принял(а) клиента:' + '(' + call.from_user.username + ')')
          markup = types.InlineKeyboardMarkup(row_width=1)
          btn1 = types.InlineKeyboardButton('Другой тип номера',callback_data="🇺🇿")
          markup.add(btn1)
          bot.send_message(user_chats,"Извините в данное время(указанное вами дате)нет свободных номеров.", reply_markup=markup,parse_mode='Markdown')
    
    if call.data == "?":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="Информация от бота: ", reply_markup=None)
            bot.send_message(call.message.chat.id,call.from_user.first_name + ' заметил(а) ошибку в анкете:' + '(' + call.from_user.username + ')')
            markup = types.InlineKeyboardMarkup(row_width=1)
            btn1 = types.InlineKeyboardButton('Заново🔄',callback_data="🇺🇿")           
            markup.add(btn1)
            bot.send_message(user_chats,"Вы допустили ошибку в анкете, пожалуйста заполните заново.", reply_markup=markup,parse_mode='Markdown')
########################################################################################################################
#2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222#
    if call.data =='TWO':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('ДА',callback_data="YES-2")
        btn2 = types.InlineKeyboardButton('НЕТ',callback_data='🇺🇿')            
        markup.add(btn1,btn2)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Вы точно хотите бронировать НОМЕР ?", reply_markup=markup,parse_mode='Markdown')
    if call.data == "YES-2":
                chat_id =call.message.chat.id
                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                msg_2 = bot.send_message(chat_id, "Отправьте ваш Ф.И.О.")
                bot.register_next_step_handler(msg_2, process_name_step_2)    
######################################################################################################################
    if call.data =='THREE':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('ДА',callback_data="YES-3")
        btn2 = types.InlineKeyboardButton('НЕТ',callback_data='🇺🇿')            
        markup.add(btn1,btn2)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Вы точно хотите бронировать НОМЕР ?", reply_markup=markup,parse_mode='Markdown')
    if call.data == "YES-3":
                chat_id =call.message.chat.id
                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                msg_3 = bot.send_message(chat_id, "Отправьте ваш Ф.И.О.")
                bot.register_next_step_handler(msg_3, process_name_step_3)  
    if call.data =='LUX':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('ДА',callback_data="YES-4")
        btn2 = types.InlineKeyboardButton('НЕТ',callback_data='🇺🇿')            
        markup.add(btn1,btn2)
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(call.message.chat.id, "Вы точно хотите бронировать НОМЕР ?", reply_markup=markup,parse_mode='Markdown')
    if call.data == "YES-4":
                chat_id =call.message.chat.id
                bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                msg_4 = bot.send_message(chat_id, "Отправьте ваш Ф.И.О.")
                bot.register_next_step_handler(msg_4, process_name_step_4)
def process_name_step_1(message):
            chat_id = message.chat.id
            name = message.text
            user = User(name)
            user_dict[chat_id] = user        
            msg_1 = bot.send_message(chat_id, 'Отправьте ваш НОМЕР ТЕЛЕФОНА\nК примеру: 99 123 45 67')
            bot.register_next_step_handler(msg_1, process_age_step_1)
  
def process_age_step_1(message):
            chat_id = message.chat.id
            age = message.text
            user = user_dict[chat_id]
            user.age = age
            msg_1 = bot.send_message(chat_id, 'На какое число желаете забронировать?\nК примеру: 31.12.22')
            bot.register_next_step_handler(msg_1, process_language_step_1)    
      
def process_language_step_1(message):
            chat_id = message.chat.id
            language = message.text
            user = user_dict[chat_id]
            user.languages = language
            msg_1 = bot.send_message(chat_id, 'До какого числа желаете забронировать?\nК примеру: 3.01.23')
            bot.register_next_step_handler(msg_1, process_git_acc_step_1)
      
def process_git_acc_step_1(message):
            chat_id = message.chat.id
            git_acc1 = message.text
            user = user_dict[chat_id]
            user.git_acc = git_acc1
            msg_1 = bot.send_message(chat_id, 'Можете отправить нам допольнительную информацию(примечание)\nК примеру:\n-Соединить кровать\n-Включите кондитционер до нашего прихода.')
            bot.register_next_step_handler(msg_1, process_want_admin_step_1)
      
def process_want_admin_step_1(message):
            global user_chats
            chat_id = message.chat.id
            want_adm = message.text
            name = message.from_user.username
            name1 = message.from_user.first_name
            user = user_dict[chat_id]
            user.want_admin = want_adm
            bot.send_message(message.from_user.id, 
                                        f"<i><b>При отправке выше требованных данных пожалуйста подождите подтверждение от администратора гостиницы</b></i>\n\n"
                                     + f'Ф.И.О. - {user.name} \n'
                                     + f'Дата приезда - {user.age}\n'
                                     + f'Желает побывать до этого срока  -  {user.languages} \n'
                                     + f'Примечание  -  {user.git_acc} \n',parse_mode="html")
      
            markup = types.InlineKeyboardMarkup()
            site_btn = types.InlineKeyboardButton( text='Принять',  callback_data='yes_1')
            site_btn1 = types.InlineKeyboardButton(text='Отклонить', callback_data='no')
            site_btn2 =types.InlineKeyboardButton(text='Ошибка в анкете',callback_data="?")
            markup.add(site_btn, site_btn1,site_btn2)
            user_chats = message.from_user.id
            bot.send_message(config.groupid,
                                       f"<b><ins>НУЖЕН ОДНОМЕСТНЫЙ НОМЕР!</ins></b>\n\n"
                                     + f"<i><b>Регистрация(Администрация)</b></i>\n\n"
                                     + f'Заявка от ' + '@'+name + ' (' + name1 + ') ' + '\n'
                                     + f'Ф.И.О. - {user.name} \n'
                                     + f'Дата приезда  -  {user.age} \n'
                                     + f'Желает побывать до этого срока -  {user.languages} \n'
                                     + f'Примечание -  {user.git_acc} \n'
                                     + f'ID человека = {user_chats}',parse_mode="html")
      
            bot.send_message(config.groupid,
                               f"<b><ins>НУЖЕН ОДНОМЕСТНЫЙ НОМЕР!</ins></b>\n\n"
                             + f'Заявка от ' + '@'+ name + ' (' + name1 + ') ' + '\n'
                             + f'Ф.И.О. - {user.name} \n'
                             + f'Дата приезда  -  {user.age} \n'
                             + f'Желает побывать до этого срока -  {user.languages} \n'
                             + f'Примечание -  {user.git_acc} \n'
                             + f'ID человека = {user_chats}', reply_markup=markup,parse_mode="html")
######################################################################################################################
######################################################################################################################
def process_name_step_2(message):
            chat_id = message.chat.id
            name = message.text
            user = User(name)
            user_dict[chat_id] = user        
            msg_2 = bot.send_message(chat_id, 'Отправьте ваш НОМЕР ТЕЛЕФОНА\nК примеру: 99 123 45 67')
            bot.register_next_step_handler(msg_2, process_age_step_2)
  
def process_age_step_2(message):
            chat_id = message.chat.id
            age = message.text
            user = user_dict[chat_id]
            user.age = age
            msg_2 = bot.send_message(chat_id, 'На какое число желаете забронировать?\nК примеру: 31.12.22')
            bot.register_next_step_handler(msg_2, process_language_step_2)    
      
def process_language_step_2(message):
            chat_id = message.chat.id
            language = message.text
            user = user_dict[chat_id]
            user.languages = language
            msg_2 = bot.send_message(chat_id, 'До какого числа желаете забронировать?\nК примеру: 3.01.23')
            bot.register_next_step_handler(msg_2, process_git_acc_step_2)
      
def process_git_acc_step_2(message):
            chat_id = message.chat.id
            git_acc1 = message.text
            user = user_dict[chat_id]
            user.git_acc = git_acc1
            msg_2 = bot.send_message(chat_id, 'Можете отправить нам допольнительную информацию(примечание)\nК примеру:\n-Соединить кровать\n-Включите кондитционер до нашего прихода.')
            bot.register_next_step_handler(msg_2, process_want_admin_step_2)
      
def process_want_admin_step_2(message):
            global user_chats
            chat_id = message.chat.id
            want_adm = message.text
            name = message.from_user.username
            name1 = message.from_user.first_name
            user = user_dict[chat_id]
            user.want_admin = want_adm
            bot.send_message(message.from_user.id, 
                                       f"<i><b>При отправке выше требованных данных пожалуйста подождите подтверждение от администратора гостиницы</b></i>\n\n"
                                     + f'Ф.И.О. - {user.name} \n'
                                     + f'Дата приезда - {user.age}\n'
                                     + f'Желает побывать до этого срока  -  {user.languages} \n'
                                     + f'Примечание  -  {user.git_acc} \n',parse_mode="html")
      
            markup = types.InlineKeyboardMarkup()
            site_btn = types.InlineKeyboardButton( text='Принять',  callback_data='yes_2')
            site_btn1 = types.InlineKeyboardButton(text='Отклонить', callback_data='no')
            site_btn2 =types.InlineKeyboardButton(text='Ошибка в анкете',callback_data="?")
            markup.add(site_btn, site_btn1,site_btn2)
            user_chats = message.from_user.id
            bot.send_message(config.groupid,
                                       f"<b><ins>НУЖЕН ДВУХМЕСТНЫЙ СТАНДАРТ!</ins></b>\n\n"
                                     + f"<i><b>Регистрация(Администрация)</b></i>\n\n"
                                     + f'Заявка от ' + '@'+name + ' (' + name1 + ') ' + '\n'
                                     + f'Ф.И.О. - {user.name} \n'
                                     + f'Дата приезда  -  {user.age} \n'
                                     + f'Желает побывать до этого срока -  {user.languages} \n'
                                     + f'Примечание -  {user.git_acc} \n'
                                     + f'ID человека = {user_chats}',parse_mode="html")
      
            bot.send_message(config.groupid,
                               f"<b><ins>НУЖЕН ДВУХМЕСТНЫЙ СТАНДАРТ!</ins></b>\n\n"
                             + f'Заявка от ' + '@'+ name + ' (' + name1 + ') ' + '\n'
                             + f'Ф.И.О. - {user.name} \n'
                             + f'Дата приезда  -  {user.age} \n'
                             + f'Желает побывать до этого срока -  {user.languages} \n'
                             + f'Примечание -  {user.git_acc} \n'
                             + f'ID человека = {user_chats}', reply_markup=markup,parse_mode="html")
######################################################################################################################
######################################################################################################################
def process_name_step_3(message):
            chat_id = message.chat.id
            name = message.text
            user = User(name)
            user_dict[chat_id] = user        
            msg_3 = bot.send_message(chat_id, 'Отправьте ваш НОМЕР ТЕЛЕФОНА\nК примеру: 99 123 45 67')
            bot.register_next_step_handler(msg_3, process_age_step_3)
  
def process_age_step_3(message):
            chat_id = message.chat.id
            age = message.text
            user = user_dict[chat_id]
            user.age = age
            msg_3 = bot.send_message(chat_id, 'На какое число желаете забронировать?\nК примеру: 31.12.22')
            bot.register_next_step_handler(msg_3, process_language_step_3)    
      
def process_language_step_3(message):
            chat_id = message.chat.id
            language = message.text
            user = user_dict[chat_id]
            user.languages = language
            msg_3 = bot.send_message(chat_id, 'До какого числа желаете забронировать?\nК примеру: 3.01.23')
            bot.register_next_step_handler(msg_3, process_git_acc_step_3)
      
def process_git_acc_step_3(message):
            chat_id = message.chat.id
            git_acc1 = message.text
            user = user_dict[chat_id]
            user.git_acc = git_acc1
            msg_3 = bot.send_message(chat_id, 'Можете отправить нам допольнительную информацию(примечание)\nК примеру:\n-Соединить кровать\n-Включите кондитционер до нашего прихода.')
            bot.register_next_step_handler(msg_3, process_want_admin_step_3)
      
def process_want_admin_step_3(message):
            global user_chats
            chat_id = message.chat.id
            want_adm = message.text
            name = message.from_user.username
            name1 = message.from_user.first_name
            user = user_dict[chat_id]
            user.want_admin = want_adm
            bot.send_message(message.from_user.id, 
                                        f"<i><b>При отправке выше требованных данных пожалуйста подождите подтверждение от администратора гостиницы</b></i>\n\n"
                                     + f'Ф.И.О. - {user.name} \n'
                                     + f'Дата приезда - {user.age}\n'
                                     + f'Желает побывать до этого срока  -  {user.languages} \n'
                                     + f'Примечание  -  {user.git_acc} \n',parse_mode="html")
      
            markup = types.InlineKeyboardMarkup()
            site_btn = types.InlineKeyboardButton( text='Принять',  callback_data='yes_3')
            site_btn1 = types.InlineKeyboardButton(text='Отклонить', callback_data='no')
            site_btn2 =types.InlineKeyboardButton(text='Ошибка в анкете',callback_data="?")
            markup.add(site_btn, site_btn1,site_btn2)
            user_chats = message.from_user.id
            bot.send_message(config.groupid,
                                       f"<b><ins>НУЖЕН ТРЕХМЕСТНЫЙ СТАНДАРТ!</ins></b>\n\n"
                                     + f"<i><b>Регистрация(Администрация)</b></i>\n\n"
                                     + f'Заявка от ' + '@'+name + ' (' + name1 + ') ' + '\n'
                                     + f'Ф.И.О. - {user.name} \n'
                                     + f'Дата приезда  -  {user.age} \n'
                                     + f'Желает побывать до этого срока -  {user.languages} \n'
                                     + f'Примечание -  {user.git_acc} \n'
                                     + f'ID человека = {user_chats}',parse_mode="html")
      
            bot.send_message(config.groupid,
                               f"<b><ins>НУЖЕН ТРЕХМЕСТНЫЙ СТАНДАРТ!</ins></b>\n\n"
                             + f'Заявка от ' + '@'+ name + ' (' + name1 + ') ' + '\n'
                             + f'Ф.И.О. - {user.name} \n'
                             + f'Дата приезда  -  {user.age} \n'
                             + f'Желает побывать до этого срока -  {user.languages} \n'
                             + f'Примечание -  {user.git_acc} \n'
                             + f'ID человека = {user_chats}', reply_markup=markup,parse_mode="html")
######################################################################################################################
######################################################################################################################                          
def process_name_step_4(message):
            chat_id = message.chat.id
            name = message.text
            user = User(name)
            user_dict[chat_id] = user        
            msg_4 = bot.send_message(chat_id, 'Отправьте ваш НОМЕР ТЕЛЕФОНА\nК примеру: 99 123 45 67')
            bot.register_next_step_handler(msg_4, process_age_step_4)
  
def process_age_step_4(message):
            chat_id = message.chat.id
            age = message.text
            user = user_dict[chat_id]
            user.age = age
            msg_4 = bot.send_message(chat_id, 'На какое число желаете забронировать?\nК примеру: 31.12.22')
            bot.register_next_step_handler(msg_4, process_language_step_4)    
      
def process_language_step_4(message):
            chat_id = message.chat.id
            language = message.text
            user = user_dict[chat_id]
            user.languages = language
            msg_4 = bot.send_message(chat_id, 'До какого числа желаете забронировать?\nК примеру: 3.01.23')
            bot.register_next_step_handler(msg_4, process_git_acc_step_4)
      
def process_git_acc_step_4(message):
            chat_id = message.chat.id
            git_acc1 = message.text
            user = user_dict[chat_id]
            user.git_acc = git_acc1
            msg_4 = bot.send_message(chat_id, 'Можете отправить нам допольнительную информацию(примечание)\nК примеру:\n-Соединить кровать\n-Включите кондитционер до нашего прихода.')
            bot.register_next_step_handler(msg_4, process_want_admin_step_4)
      
def process_want_admin_step_4(message):
            global user_chats
            chat_id = message.chat.id
            want_adm = message.text
            name = message.from_user.username
            name1 = message.from_user.first_name
            user = user_dict[chat_id]
            user.want_admin = want_adm
            bot.send_message(message.from_user.id, 
                                        f"<i><b>При отправке выше требованных данных пожалуйста подождите подтверждение от администратора гостиницы</b></i>\n\n"
                                     + f'Ф.И.О. - {user.name} \n'
                                     + f'Дата приезда - {user.age}\n'
                                     + f'Желает побывать до этого срока  -  {user.languages} \n'
                                     + f'Примечание  -  {user.git_acc} \n',parse_mode="html")
      
            markup = types.InlineKeyboardMarkup()
            site_btn = types.InlineKeyboardButton( text='Принять',  callback_data='yes_4')
            site_btn1 = types.InlineKeyboardButton(text='Отклонить', callback_data='no')
            site_btn2 =types.InlineKeyboardButton(text='Ошибка в анкете',callback_data="?")
            markup.add(site_btn, site_btn1,site_btn2)
            user_chats = message.from_user.id
            bot.send_message(config.groupid,
                                       f"<b><ins>СЕМЕЙНЫЙ ЛЮКС НОМЕР!</ins></b>\n\n"
                                     + f"<i><b>Регистрация(Администрация)</b></i>\n\n"
                                     + f'Заявка от ' + '@'+name + ' (' + name1 + ') ' + '\n'
                                     + f'Ф.И.О. - {user.name} \n'
                                     + f'Дата приезда  -  {user.age} \n'
                                     + f'Желает побывать до этого срока -  {user.languages} \n'
                                     + f'Примечание -  {user.git_acc} \n'
                                     + f'ID человека = {user_chats}',parse_mode="html")
      
            bot.send_message(config.groupid,
                               f"<b><ins>СЕМЕЙНЫЙ ЛЮКС НОМЕР!</ins></b>\n\n"
                             + f'Заявка от ' + '@'+ name + ' (' + name1 + ') ' + '\n'
                             + f'Ф.И.О. - {user.name} \n'
                             + f'Дата приезда  -  {user.age} \n'
                             + f'Желает побывать до этого срока -  {user.languages} \n'
                             + f'Примечание -  {user.git_acc} \n'
                             + f'ID человека = {user_chats}', reply_markup=markup,parse_mode="html")
@bot.message_handler(content_types=['successful_payment'])
def got_payment(message, res=False):
                global user_chats
                chat_id = message.chat.id
                want_adm = message.text
                name = message.from_user.username
                name1 = message.from_user.first_name
                bot.send_message(message.chat.id,'ПЛАТЕЖ УСПЕШНО ПРОВЕДЁН В РАЗМЕРЕ! ***{} {}*** ЖДЕМ ВАС В ГОСТИ!'.format(message.successful_payment.total_amount / 100, message.successful_payment.currency),parse_mode='Markdown')
                bot.send_message(config.groupid,
                               f'Оплачен Инвойс клиентом:' + '@'+ name + ' (' + name1 + ') ' + '\n')
@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Просим прошение! ПРОИЗОШЛО МАЛЕНЬНОЕ ОШИБКА! Попробуйте заплатить еще раз через несколько минут ")


bot.remove_webhook()
bot.polling()