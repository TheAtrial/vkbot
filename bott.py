# -*- coding: utf-8 -*-
# vkbott v0.1 бот пересылает любые сообщения на почту, которая синхронизируется с crm и создает на каждое сообщение боту новое обращение.
import vk_api
import random
import smtplib
from vk_api.longpoll import VkLongPoll, VkEventType
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})
# паблик API-ключ
token = ""

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Подключаем лонгпол
longpoll = VkLongPoll(vk)
   
print("Бот запущен")

for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
     
            # Сообщение от пользователя
            request = event.text
            msg = "привет";
            msg1 = "бай";
            msg2 = "Ваше обращение будет рассмотренно!";
            # Каменная логика ответа
            if request == "привет":
                vk.method('messages.send', {
                'user_id': event.user_id,
                'message': msg,
                'random_id': random.randint(1, 1000000)
                })
            elif request == "пока":
                vk.method('messages.send', {
                'user_id': event.user_id,
                'message': msg1,
                'random_id': random.randint(1, 1000000)
                })
            else:
				
                vk.method('messages.send', {
                'user_id': event.user_id,
                'message': msg2,
                'random_id': random.randint(1, 1000000)
                }),

                # создаем мульиконтейнер
                msg = MIMEMultipart()
                 
                # параметры почты
                password = ""
                msg['From'] = ""
                msg['To'] = ""
                msg['Subject'] = "Обращение"
                message = request
				
                msg.attach(MIMEText(message, 'plain'))
 
                #создаем почтовый сервис
                server = smtplib.SMTP('smtp.mail.ru: 2525')
                server.starttls()
                # логинимся
                server.login(msg['From'], password)               
                # отправляем на почту.
                server.sendmail(msg['From'], msg['To'], msg.as_string()) 
                server.quit()
                print ("successfully sent email ")


