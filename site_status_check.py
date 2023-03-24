import requests
import telebot
import sched, time

s = sched.scheduler(time.time, time.sleep)



# Функция таймера
def timer_for_bot():
    s.enter(1800, 1, timer_for_bot) #<-- 1 раз в 1800 секунд запрос
    print(time.time())

    #Словарь вариантов ответа сайта nat_com.ru
    all_responses_nat_com = {
        200: '[nat-com] Всё окей (200)',
        400: '[nat-com] Ошибка (400)',
        400: '[nat-com] Cтраница не найдена (404)',
        503: '[nat-com] Сервис недоступен (503)'
    }

    # Словарь вариантов ответа сайта безшва.рф
    all_responses_bezshva = {
        200: '[безшва] Всё окей (200)',
        400: '[безшва] Ошибка (400)',
        400: '[безшва] Cтраница не найдена (404)',
        503: '[безшва] Сервис недоступен (503)'
    }

    def request_natcom(all_responses_nat_com):
        resp1 = []
        r = requests.get('https://nat-com.ru/')
        for key, value in all_responses_nat_com.items():
            if r.status_code == key:
                resp1.append(value)
        return resp1

    def request_bezshva(all_responses_bezshva):
        resp2 = []
        r = requests.get('https://безшва.рф')
        for key, value in all_responses_bezshva.items():
            if r.status_code == key:
                resp2.append(value)
        return resp2


    API_TOKEN = '363684825:AAGjj4rdAoDZScibOTIczoe0Uu5QVDvHMWY'
    bot = telebot.TeleBot(API_TOKEN)
    users = [-905217525]

    msg_text1 = request_natcom(all_responses_nat_com)
    msg_text2 = request_bezshva(all_responses_bezshva)

    def send_log_msg1(msg_text1):
        for user in users:
            print(msg_text1)
            msg = msg_text1
            print(msg)
            bot.send_message(user, msg)

    def send_log_msg2(msg_text2):
        for user in users:
            print(msg_text2)
            msg = msg_text2
            print(msg)
            bot.send_message(user, msg)

    send_log_msg1(msg_text1)
    send_log_msg2(msg_text2)

timer_for_bot()
s.run()