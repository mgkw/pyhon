import json

import urllib3
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

urllib3.disable_warnings()
import requests
import telebot
from telebot import TeleBot
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)  # Outputs debug messages to console.

bot: TeleBot = telebot.TeleBot('1270470792:AAG7KSOty2XogSd9OYOURJfc2DvuG-c2Gqk')

OFFSET = 127462 - ord('A')


def flag(code):
    code = code.upper()
    return chr(ord(code[0]) + OFFSET) + chr(ord(code[1]) + OFFSET)


HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/51.0.2704.103 Safari/537.36', 'accept': '*/*'}


@bot.message_handler(commands=['start'])
def start(message):
    neme = message.from_user.first_name
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIBeF6qmrNYQQ6-tyzFg2etllCl5xDRAALIAQACVp29Ch5kbWu8BAS4GQQ', reply_to_message_id=message.message_id)
    keyboard = InlineKeyboardMarkup()
    callback_button_1 = InlineKeyboardButton(text=" المساعدة ⁉️ ", callback_data='dat')
    callback_button_2 = InlineKeyboardButton(text="Dev By ✨ ", url='t.me/itsmgkw')
    callback_button_3 = InlineKeyboardButton(text="قناة البوت  🎗 ", url='https://t.me/joinchat/AAAAAENpSof3pcmPGZjp-g')
    keyboard.add(callback_button_1, callback_button_2)
    keyboard.add(callback_button_3)
    bot.send_message(message.chat.id,
                     text=" مرحبـا بك {} 👋🏻 في بوت يقدم لك تحديثات فايروس كورونا في جميع انحاء العالم ما عليك فقط الضغط على المساعدة للبدء 💎 . ".format(
                         neme), reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data == 'dat')
def callbackin(call):
    markup = InlineKeyboardMarkup()
    callback_button = InlineKeyboardButton(text="القائمة الرئسية 🦠", callback_data='bak')
    markup.add(callback_button)
    if call.message:
        if call.data == "dat":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='هلاً بك في قائمة المساعدة ❗️'
                                       '\n'




                                       '\n/covid - للحصول على احداثيات  مباشرة'
                                       '\n'
                                       '\n هناك طريقين للبحث عن البلدان ⁉️'

                                       '\n '
                                       '\n/country - االبحث على بلد معين'
                                       '\n'
                                       '\n/covid - ارسل الامر مع اسم البلد الصحيح'
                                       "ّ"
                                       "\n"
                                       '\n - مثال يوضح طريقة الاستعمال   '

                                       '\n/covid Iraq  '
                                       '\n '
                                       '\n/help - لمشاهدة المزيد من المعلومات'

                                  , reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'bak')
def start(message1):
    keyboa1 = InlineKeyboardMarkup()
    callback_button_1 = InlineKeyboardButton(text=" المساعدة ⁉️ ", callback_data='dat')
    callback_button_2 = InlineKeyboardButton(text="Dev By ✨ ", url='t.me/itsmgkw')
    callback_button_3 = InlineKeyboardButton(text="قناة البوت  🎗 ", url='https://t.me/joinchat/AAAAAENpSof3pcmPGZjp-g')
    keyboa1.add(callback_button_1, callback_button_2)
    keyboa1.add(callback_button_3)
    if message1:
        if message1.data == "bak":
            bot.edit_message_text(chat_id=message1.message.chat.id, message_id=message1.message.message_id,
                                  text="مرحباً مجدداً 🦠 " + message1.from_user.first_name, reply_markup=keyboa1)


@bot.message_handler(commands=['help'])
def start(message):
    hyu = InlineKeyboardMarkup()

    callbackin_1 = InlineKeyboardButton(text="Dev By ✨ ", url='t.me/itsmgkw')
    hyu.add(callbackin_1)

    bot.send_message(message.chat.id,
                     text="سلام البوت مخصص لاحداثيات فايروس كورونا في العالم كل 10 دقائق اي مشكلة او استفسار او قتراح حاجو المطور  ",
                     reply_markup=hyu)


@bot.message_handler(commands=['covid'])
def get_coronavirus_information(message):
    text = message.text[7:]
    if len(text) == 0:
        r = requests.get(
            'https://corona.lmao.ninja/v2/all')
        response = r.json()
        bot.send_message(parse_mode='HTML',
                         chat_id=message.chat.id,
                         text=
                         "🦠 إجمالي الإصابات : "
                         + str(response['cases'])
                         + "\n🧪 حالات اليـوم : "
                         + str(response['todayCases'])
                         + "\n💀️ إجـمالي الوفيات : "
                         + str(response['deaths'])
                         + "\n⚰️ وفـيات الـيوم : "
                         + str(response['todayDeaths'])
                         + "\n➕ الـتـعـافـي : "
                         + str(response['recovered'])
                         + "\n🟢 نــشــط : "
                         + str(response['active'])
                         + "\n⛔ الحالات الحرجة : "
                         + str(response['critical'])
                         + "\n🔬 تـم اخــتبـاره : "
                         + str(response['tests'])
                         + "\n🚫 الـبـلـدان المُـتضـرره : "
                         + str(response['affectedCountries'])
                         + "\n\n♻️ للتحديث اضغط\n /covid"

                         )
    else:
        with open('countries.json', 'r') as f:
            countries_dict = json.load(f)
        try:
            country = [obj for obj in countries_dict if text == obj['en_name'] or text == obj['ru_name']]
            r = requests.get(
                'https://corona.lmao.ninja/v2/countries/' + country[0]['en_name'])
            response = r.json()
            bot.send_message(parse_mode='HTML',
                             chat_id=message.chat.id,
                             text=" <b> البلد : "
                                  + flag(response['countryInfo']['iso2'])
                                  + " " + text
                                  + "</b>\n🦠 إجـمالي الإصابـات : "
                                  + str(response['cases'])
                                  + "\n🧪 حـالات اليـوم :"
                                  + str(response['todayCases'])
                                  + "\n⚰️ إجـمالي الوفيات :"
                                  + str(response['deaths'])
                                  + "\n⚰️ وفـيات الـيوم : "
                                  + str(response['todayDeaths'])
                                  + "\n➕ الـتـعـافـي : "
                                  + str(response['recovered'])
                                  + "\n🔬 تـم اخــتبـاره :"
                                  + str(response['tests'])
                             )
        except:
            bot.reply_to(message,
                         '  هذا البلد ليس في قاعدة البيانات\n تأكد من الاسم الصجيج او جرب اسم يبدأ بحرف كبير \n مثال \n> Iraq .')


@bot.message_handler(commands=['country'])
def hello(massage):
    bot.send_message(massage.chat.id, 'ادخل اسم البد 🌍🔎 .\n'
                                      'مثال ❕ : US, Iraq , Iran , Italy...')

    @bot.message_handler()
    def stat_couantry(massage):
        url_api = 'https://covid2019-api.herokuapp.com/v2/country/' + massage.text
        corona = requests.get(url_api, headers=HEADERS)
        try:
            dt = corona.json()["dt"]
            location = corona.json()["data"]["location"]
            deaths = corona.json()["data"]["deaths"]
            recovered = corona.json()["data"]["recovered"]
            confirmed = corona.json()["data"]["confirmed"]
            bot.send_message(massage.chat.id, f'الـبلـد 🌍 : {location}\n'
                                              f'الحالات المؤكدة 📌 : {confirmed}\n'
                                              f'اجمالي الوفيات 💀 : {deaths}\n'
                                              f'التعافي 🦠 : {recovered}\n'
                                              f'-----------\n'
                                              f'اخر تحديث ⏳ {dt}\n')


        except KeyError:
            bot.reply_to(massage, f' عذراً البلد غير متوفر\n تأكد من صحة الاسم او جرب اسماً اخر 🔰..')


if __name__ == '__main__':
    bot.polling(none_stop=True)


@bot.message_handler()
def stat_couantry(massage):
    url_api = 'https://corona.lmao.ninja/v2/countries/' + massage.text
    corona = requests.get(url_api, headers=HEADERS)
    try:
        dt = corona.json()["dt"]
        location = corona.json()["data"]["location"]
        deaths = corona.json()["data"]["deaths"]
        recovered = corona.json()["data"]["recovered"]
        confirmed = corona.json()["data"]["confirmed"]
        bot.send_message(massage.chat.id, f'Країна : {location}\n'
                                          f'Зафіксовано випадків : {confirmed}\n'
                                          f'Смертей : {deaths}\n'
                                          f'Одужало : {recovered}\n'
                                          f'-----------\n'
                                          f'Інформація актуальна на {dt}\n')
    except KeyError:
        bot.send_message(massage.chat.id, f'Країни не знайдено. Спробуйте ще раз!')


if __name__ == '__main__':
    bot.polling(none_stop=True)
