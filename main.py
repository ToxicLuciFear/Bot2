# Телеграм-бот v.002 - бот создаёт меню, присылает собачку, и анекдот

import telebot  # pyTelegramBotAPI	4.3.1
import requests
import bs4
import json
from telebot import types

bot = telebot.TeleBot('5191652585:AAFgiV9xp8-bkRIXikmXrdnMKXygMOWcagI')  # Создаем экземпляр бота


# -----------------------------------------------------------------------
def inputBot(message, text):
    a = []

    def ret(message):
        a.clear()
        a.append(message.text)
        return False

    a.clear()
    mes = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, ret)
    while a == []:
        pass
    return a[0]


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    btn2 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке ПаЙтон".format(
                         message.from_user), reply_markup=markup)


# -----------------------------------------------------------------------
# Получение сообщений от юзера
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Главное меню" or ms_text == "👋 Главное меню" or ms_text == "Вернуться в главное меню":  # ..........
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Развлечения")
        btn2 = types.KeyboardButton("Рандомное Аниме!!!")
        btn3 = types.KeyboardButton("Управление")
        btn4 = types.KeyboardButton("ДЗ")
        back = types.KeyboardButton("Помощь")
        markup.add(btn1, btn2, btn3, btn4, back)
        bot.send_message(chat_id, text="Вы в главном меню", reply_markup=markup)

    elif ms_text == "Развлечения":  # ..................................................................................
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Прислать собаку")
        btn2 = types.KeyboardButton("Прислать анекдот")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(chat_id, text="Развлечения", reply_markup=markup)

    elif ms_text == "/dog" or ms_text == "Прислать собаку":  # .........................................................

        bot.send_photo(message.chat.id, Get_dogURL())

    elif ms_text == "Прислать анекдот":  # .............................................................................
        bot.send_message(chat_id, text=get_anekdot())

    elif ms_text == "Рандомное Аниме!!!":
        bot.send_message(chat_id, get_anime())

    elif ms_text == "Управление":  # ...................................................................................
        bot.send_message(chat_id, text="еще не готово...")

    elif ms_text == "Помощь" or ms_text == "/help":  # .................................................................
        bot.send_message(chat_id, "Автор: Твой Отец")
        key1 = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/ToxicLucFear")
        key1.add(btn1)
        img = open('404.png', 'rb')
        bot.send_photo(message.chat.id, img, reply_markup=key1)
    elif ms_text == "ДЗ":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        z1 = types.KeyboardButton("I")
        z2 = types.KeyboardButton("II")
        z3 = types.KeyboardButton("III")
        z45 = types.KeyboardButton("IV-V")
        z6 = types.KeyboardButton("VI")
        z7 = types.KeyboardButton("VII")
        z8 = types.KeyboardButton("VIII")
        z9 = types.KeyboardButton("IX")
        z10 = types.KeyboardButton("X")
        back = types.KeyboardButton("Главное меню")
        markup.add(z1, z2, z3, z45, z6, z7, z8, z9, z10, back)
        bot.send_message(chat_id, text="ДЗ", reply_markup=markup)
    elif ms_text == "I":
        a = inputBot(message, "Введите имя")
        bot.send_message(chat_id, text="Теперь я знаю что тебя зовут " + a)
    elif ms_text == "II":
        a = inputBot(message, "Введите возраст")
        bot.send_message(chat_id, text="О, так тебе уже " + a + " лет")
    elif ms_text == "III":
        a = inputBot(message, "Введите имя") * 5
        bot.send_message(chat_id, a)
    elif ms_text == "IV-V":
        a = inputBot(message, "Введите имя")
        n = int(inputBot(message, "Введите возраст"))
        bot.send_message(chat_id, text="Ну здарова " + a)
        if n >= 60:
            bot.send_message(chat_id, text="Ты что дед?")
        elif n <= 6:
            bot.send_message(chat_id, text="Где твои родители?")
        elif 6 < n < 18:
            bot.send_message(chat_id, text="Что по матеше задали?")
        elif 18 <= n < 60:
            bot.send_message(chat_id, text="Сколько зарабатываешь?")
    elif ms_text == "VI":
        a = inputBot(message, "Введите имя")
        n = len(a)
        bot.send_message(chat_id, a[1:n - 1:])
        bot.send_message(chat_id, a[::-1])
        bot.send_message(chat_id, a[-3::])
        bot.send_message(chat_id, a[:5:])
    elif ms_text == "VII":
        a = inputBot(message, "Введите имя")
        n = int(inputBot(message, "Введите возраст"))
        bot.send_message(chat_id, "Длина имени " + str(len(a)))
        n1 = (n // 10) + (n % 10)
        n2 = (n // 10) * (n % 10)
        bot.send_message(chat_id, "Сумма цифр возраста= " + str(n1) + " А их произведение= " + str(n2))
    elif ms_text == "VIII":
        un = inputBot(message, "Введите имя")
        nu = str(str.upper(un))
        nl = str(str.lower(un))
        bot.send_message(chat_id, str(str.upper(un)))
        bot.send_message(chat_id, str(str.lower(un)))
        bot.send_message(chat_id, str(nu[0:1:]) + str(nl[1::]))
        bot.send_message(chat_id, str(nl[0:1:]) + str(nu[1::]))
    elif ms_text == "IX":
        un = inputBot(message, "Введите имя")
        ua = int(inputBot(message, "Введите возраст"))
        a = 0
        spaces = 0
        for i in range(0, len(un)):
            if un[i] == ' ':
                bot.send_message(chat_id, "Пробел в имени не допустим")
                spaces += 1
                break
            else:
                spaces = 0
        if spaces == 0:
            bot.send_message(chat_id, "Имя введено правильно")
        if ua > 150 or ua < 0:
            bot.send_message(chat_id, "Вы ввели не корректный возраст")
        else:
            bot.send_message(chat_id, "Возраст введён правильно")
    elif ms_text == "X":
        bot.send_message(chat_id, "Помоги решить плиз")
        bot.send_message(chat_id, "1/2*x*y+(47-x-y)*(x/3+y/4)")
        v = int(inputBot(message, "Жду ответ"))
        if v == 282:
            bot.send_message(chat_id, "Ты что киборг???????????????")
        else:
            bot.send_message(chat_id, "Ну.........ты хотя бы попытался)")
    else:  # ...........................................................................................................
        bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: " + ms_text)


def get_anekdot():
    array_anekdots = []
    req_anek = requests.get('http://anekdotme.ru/random')
    soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
    result_find = soup.select('.anekdot_text')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
    return array_anekdots[0]

def get_anime():
    array_anime = []
    req_anime = requests.get('https://manga-chan.me/manga/random')
    soup = bs4.BeautifulSoup(req_anime.text, "html.parser")
    result_find = soup.findAll("a", class_="title_link")
    return result_find

def Get_dogURL():
    contents = requests.get("https://random.dog/woof.json").json()
    return contents["url"]

bot.polling(none_stop=True, interval=0)

print()
