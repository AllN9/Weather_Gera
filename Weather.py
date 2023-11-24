import requests
import telebot

bot = telebot.TeleBot('6391115122:AAGbHlcSycIYWC7pdF2VmnDHW3ePPCbqLyo');

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, Я подсказываю температуру на улице, напиши желаемый город!")
    else:
        city = message.text
        url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
        weather_data = requests.get(url).json()
        
        if(weather_data['cod'] == '404'):
            bot.send_message(message.from_user.id, 'Такого города нет, напишите другой!')
        else:
            temperature = round(weather_data['main']['temp'])
            message_temperature = 'Сейчас в городе' + ' ' + city + ' ' + str(temperature) + ' ' + '°C'
            bot.send_message(message.from_user.id, message_temperature)

            temperature_feels = round(weather_data['main']['feels_like'])
            message_temperature_feels = 'Ощущается как' + ' ' + str(temperature_feels) + ' ' + '°C'
            bot.send_message(message.from_user.id, message_temperature_feels)

bot.polling(none_stop=True, interval=0)