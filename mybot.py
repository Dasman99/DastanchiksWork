from confiq import TOKEN

import telebot
from telebot.types import (

InlineKeyboardButton,
InlineKeyboardMarkup,
ReplyKeyboardMarkup,
KeyboardButton
)
order = {}
order_list = {}
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    data_text = "Кукусики!"
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    menu = InlineKeyboardButton("Меню", callback_data="menu")
    markup.add(menu)
    bot.send_message(message.chat.id, text=data_text, reply_markup=markup)
    feedback_btn = InlineKeyboardButton('Оставить отзыв', callback_data='feedback')
    markup.add(feedback_btn)
    bot.send_message(message.chat.id, text=data_text, reply_markup=markup)


dict_category = {
    'first_meals': ['борщ', 'рагу', 'суп'],
    'second_meals': ['плов', 'ашпало', 'куурдак'],
    'sweets': ['фруктовый салат', 'мороженое', 'пирог'],
    'drinks': ['кола', 'спрайт', 'фанта']
}
food_prices = {
    dict_category['first_meals'][0]:350,
    dict_category['first_meals'][1]:200,
    dict_category['first_meals'][2]:150,
    dict_category['second_meals'][0]:300,
    dict_category['second_meals'][1]:170,
    dict_category['second_meals'][2]:400,
    dict_category['sweets'][0]:100,
    dict_category['sweets'][1]:70,
    dict_category['sweets'][2]:25,
    dict_category['drinks'][0]:100,
    dict_category['drinks'][1]:100,
    dict_category['drinks'][2]:100,

}
# print(food_prices)


@bot.callback_query_handler(func=lambda call: call.data == "menu")
def answer_menu_callback(call):
    message = call.message
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    keys_of_dict = dict_category.keys()
    if keys_of_dict:
        for category in keys_of_dict:
            btn = InlineKeyboardButton(category, callback_data=category)
            markup.add(btn)
        back = InlineKeyboardButton("Назад", callback_data="back_to_menu")
        markup.add(back)
        bot.edit_message_text(chat_id=message.chat.id, text="Choose a category", message_id=message.message_id,reply_markup=markup)
    else:
        bot.edit_message_text(chat_id=message.chat.id, text="Sorry, Menu not available!")


dict_category_keys = list(dict_category.keys())

@bot.callback_query_handler(func=lambda call: call.data in dict_category_keys)
def answer_category_callback(call):
    message = call.message
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    back_btn = InlineKeyboardButton('Назад', callback_data='back_to_categories')
    markup.add(back_btn)
    bot.edit_message_text(chat_id=message.chat.id, text="Choose meal", message_id=message.message_id, reply_markup=markup)
    btn = InlineKeyboardButton('Меню', callback_data='back_to_menu')
    markup.add(btn)
    if call.data == dict_category_keys[0]:
        for meal in dict_category['first_meals']:
            btn = InlineKeyboardButton(meal, callback_data=meal)
            markup.add(btn)

        bot.edit_message_text(
            chat_id=message.chat.id,
            text='Choose meal:',
            message_id=message.id,
            reply_markup=markup
            )

    elif call.data == dict_category_keys[1]:
        for meal in dict_category['second_meals']:
            btn= InlineKeyboardButton(meal, callback_data=meal)
            markup.add(btn)


        bot.edit_message_text(
            chat_id=message.chat.id,
            text='Choose meal:',
            message_id=message.id,
            reply_markup=markup
    )

    elif call.data == dict_category_keys[2]:
        for meal in dict_category['sweets']:
            btn = InlineKeyboardButton(meal, callback_data=meal)
            markup.add(btn)

        bot.edit_message_text(
            chat_id=message.chat.id,
            text='Choose sweet:',
            message_id=message.id,
            reply_markup=markup
        )

    elif call.data == dict_category_keys[3]:
        for meal in dict_category['drinks']:
            btn = InlineKeyboardButton(meal, callback_data=meal)
            markup.add(btn)

        bot.edit_message_text(
            chat_id=message.chat.id,
            text='Choose drink:',
            message_id=message.id,
            reply_markup=markup
        )

@bot.callback_query_handler(func=lambda call: str(call.data).startswith("back_to"))
def back_button(call):
    message = call.message
    if call.data == "back_to_menu":
        send_welcome_message(message)
    elif call.data == "back_to_categories":
        answer_menu_callback(call)

food_prices_keys = food_prices.keys()
food_prices_keys_list = list(food_prices_keys)

@bot.callback_query_handler(func=lambda call: call.data in food_prices_keys_list)
def get_meal_info(call):
    message = call.message
    message_date = message.date
    global order_list
    print(message_date)
    if call.data in food_prices_keys_list:
        # food_data = food_prices[call.data]
            # food_data = food_prices['борщ']
            text = f"{call.data} was added to your order. {order_list}"
            bot.send_message(message.chat.id, text=text, reply_markup=None)

@bot.message_handler(commands=['make_order'])
def make_order():
    global order_list
    for meal in order_list:
        title = meal
        count = order_list.count(meal)
        price_for_one = food_prices[title]
        total_price = count * price_for_one
        order.update({title: {
            'count': count,
            'price dor one': price_for_one,
            'total ptice': total_price
        }})

        with open("order.txt", "a") as file:
            file.write(str(order))
            order_list.clear()
            bot.send_message(message.chat.id, text="your order is completed", reply_markup=None)
        print(meal, order_list.count(meal))
@bot.message_handler(commands=['my_order'])
def show_my_order(message):
    global order_list
    if order_list:
        text = order_list
    else:
        text ='your order is empty'
    bot.send_message(message.chat.id, text =order_list)
    # if call.data in food_prices_keys_list:
    #     if call.data == "рагу":
    #         food_data = food_prices['рагу']
    #         text = f" Meal {call.data} have price {food_data} som"
    #         bot.send_message(message.chat.id, text=text, reply_markup=None)
    #
    # if call.data in food_prices_keys_list:
    #     if call.data == "суп":
    #         food_data = food_prices['суп']
    #         text = f" Meal {call.data} have price {food_data} som"
    #         bot.send_message(message.chat.id, text=text, reply_markup=None)
    #
    # if call.data in food_prices_keys_list:
    #     if call.data == "плов":
    #         food_data = food_prices['плов']
    #         text = f" Meal {call.data} have price {food_data} som"
    #         bot.send_message(message.chat.id, text=text, reply_markup=None)
    #
    # if call.data in food_prices_keys_list:
    #     if call.data == "ашпалоо":
    #         food_data = food_prices['ашпалоо']
    #         text = f" Meal {call.data} have price {food_data} som"
    #         bot.send_message(message.chat.id, text=text, reply_markup=None)
    #
    # if call.data in food_prices_keys_list:
    #     if call.data == "куурдак":
    #         food_data = food_prices['куурдак']
    #         text = f" Meal {call.data} have price {food_data} som"
    #         bot.send_message(message.chat.id, text=text, reply_markup=None)
    #
    # if call.data in food_prices_keys_list:
    #     if call.data == "фруктовый салат":
    #         food_data = food_prices['фруктовый салат']
    #         text = f" Meal {call.data} have price {food_data} som"
    #         bot.send_message(message.chat.id, text=text, reply_markup=None)
    #
    # if call.data in food_prices_keys_list:
    #     if call.data == "мороженое":
    #         food_data = food_prices['мороженое']
    #         text = f" Meal {call.data} have price {food_data} som"
    #         bot.send_message(message.chat.id, text=text, reply_markup=None)
    #
    # if call.data in food_prices_keys_list:
    #     if call.data == "пирог":
    #         food_data = food_prices['пирог']
    #         text = f" Meal {call.data} have price {food_data} som"
    #         bot.send_message(message.chat.id, text=text, reply_markup=None)
    #
    # if call.data in food_prices_keys_list:
    #     if call.data == "кола":
    #         food_data = food_prices['кола']
    #         text = f" Meal {call.data} have price {food_data} som"
    #         bot.send_message(message.chat.id, text=text, reply_markup=None)
    #
    # if call.data in food_prices_keys_list:
    #     if call.data == "спрайт":
    #         food_data = food_prices['спрайт']
    #         text = f" Meal {call.data} have price {food_data} som"
    #         bot.send_message(message.chat.id, text=text, reply_markup=None)
    #
    # if call.data in food_prices_keys_list:
    #     if call.data == "фанта":
    #         food_data = food_prices['фанта']
    #         text = f" Meal {call.data} have price {food_data} som"
    #         bot.send_message(message.chat.id, text=text, reply_markup=None)


@bot.callback_query_handler(func=lambda call: call.data == "feedback" )
def answer_of_feedback_callback(call):
    message = call.message
    print(message)
    text = "Напишите свой отзыв о нашем сервисе: "
    bot.send_message(message.chat.id, text, reply_markup=None)
    bot.register_next_step_handler(message=message, callback=get_feedback)


def get_feedback(message):
    #TODO: text, username, data
    from datetime import datetime
    text_of_message = message.text
    print(text_of_message)
    username = message.from_user.username
    print(username)
    message_date_time = message.date
    message_conv_time = datetime.fromtimestamp(message_date_time).strftime("%d-%m-%Y %H:%M:%S")
    print(message_conv_time)
    with open("reviews.txt", "a", encoding="utf-8") as file:
        text = f"""
        Time: {message_conv_time}
        Username: {username};
        Review: {text_of_message};
        """
        file.write(text)

bot.polling()