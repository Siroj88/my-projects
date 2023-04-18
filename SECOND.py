from telebot import TeleBot, types

token = "6287712593:AAFeyvIFqXz9vxvdn24kMYU9-df6DEDoa50"
mybot = TeleBot(token)


@mybot.message_handler(commands=['start'])
def boshlash(message):
    tugmalar = types.InlineKeyboardMarkup()
    tugma1 = types.InlineKeyboardButton("30 ta", callback_data="30")
    tugma2 = types.InlineKeyboardButton("15 ta", callback_data="15")
    tugmalar.add(tugma1)
    tugmalar.add(tugma2)
    mybot.send_message(message.chat.id, "Test turini tanlang ", reply_markup=tugmalar)
@mybot.callback_query_handler(func=lambda call: True)
def tugma_bos(call):
    user_id = call.message.chat.id
    if call.data == "30":
        mybot.delete_message(user_id, call.message.id)
        mybot.send_message(user_id, "30 ta")
    elif call.data == "15":
        mybot.delete_message(user_id, call.message.id)
        mybot.send_message(user_id, "15 ta")
mybot.polling()