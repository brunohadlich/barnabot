#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from communication import Communication, send_message
from time import sleep
from os import _exit

keywords_speaches = [[[u"vida"], ["Sou um matuto sofrido"]],
                     [[u'foda', u'dific', u'difíc', u'sofri', u'sofre', u'sofrê'], ["Quando eu era um matutinho tive q trabaia pra compra meu primeiro computador."]],
                     [[u'$', u'dólar', u'dolar', u'dollar'], ['Aaahh U$1,00 é tudo que eu queria.']],
                     [[u'balde'], ['Me chamaram?']],
                     [[u'merda'], ['Alguém precisando de um balde?']],
                     [[u'chulé', u'chule'], ['Não fui eu.']]
                    ]

def process_msg(text, chat_id, group_title, com):
    text = text.lower()
    for ks in keywords_speaches:
        for keyword in ks[0]:
            if keyword in text:
                index = 0
                if len(ks[1]) > 1:
                    index = randint(0, len(ks[1]) - 1)
                send_message(ks[1][index], chat_id, com)
                break

if __name__ == '__main__':
    com = Communication()
    com.on_receive_msg(process_msg)
    com.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        _exit(0)
