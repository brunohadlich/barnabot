#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from communication import Communication, send_message
from time import sleep
from os import _exit

def historia_barnabe(text, chat_id, group_title, com):
    reply = "Sou um matuto sofrido"
    text = text.lower()
    if (
        (('conte' in text) and ('vida' in text)) or
        (('quem' in text) and ('barnab' in text))
    ):
        send_message(reply, chat_id, com)
        return

def sofrencia_barnabe(text, chat_id, group_title, com):
    speaches = ["Quando eu era um matutinho tive q trabaia pra compra meu primeiro computador."]
    VIDA_DIFICIL = [u'foda', u'dific', u'difíc', u'sofri', u'sofre', u'sofrê']
    text = text.lower()
    for i in VIDA_DIFICIL:
        if i in text:
            index = randint(0,len(speaches) - 1)
            send_message(speaches[index], chat_id, com)
            break

if __name__ == '__main__':
    com = Communication()
    com.on_receive_msg(historia_barnabe)
    com.on_receive_msg(sofrencia_barnabe)
    com.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        _exit(0)
