import telebot
import os
import threading
TOKEN = '1702487152:AAEGxs01bwhUwtWf46ec2Epfd_p3XCY8qxA'

userId = [
    765549938
]
tb = telebot.TeleBot(TOKEN)

curPath = os.getcwd() +'/Polls/TelegaFiles/'


def SendMessage(message):
    artoriasDance = open(curPath +'givKa/artoriasDance.mp4','rb')
    tb.send_animation(userId[0] , artoriasDance)
    tb.send_message(userId[0], str(message))


class TelegaBot(threading.Thread):

    def run(self):
        print('Бот готов к бою')
        tb.polling()

    @tb.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bigBoss = open(curPath +'givKa/bigBoss.webp','rb')
        tb.send_message(message.chat.id,"Отвали! Здесь нечего нет,Когда будет отправлю. ЖДИ")
        tb.send_sticker(message.chat.id,bigBoss)



    
    
    
    

