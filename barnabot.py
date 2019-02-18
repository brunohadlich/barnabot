#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from communication import Communication, send_message
from time import sleep
from os import _exit
import datetime, pytz

single_keywords_speaches = [
                    [[u"vida"], [u"Sou um matuto sofrido"]],
                    [[u'foda', u'dific', u'difíc', u'sofri', u'sofre', u'sofrê'], [u"Quando eu era um matutinho tive q trabaia pra compra meu primeiro computador."]],
                    [[u'$', u'dólar', u'dolar', u'dollar'], [u'Aaahh U$1,00 é tudo que eu queria.']],
                    [[u'balde'], [u'Me chamaram?']],
                    [[u'merda'], [u'Alguém precisando de um balde?']],
                    [[u'chulé', u'chule'], [u'Não fui eu']],
                    [[u'linguagem', u'linguagens', u'java', u'javascript', u'go', u'python', u'node', u'sql'], [u'Eu programo em AngularJS']],
                    [[u'caro'], [u'Meu salário não permite, sou destitute']],
                    [[u'salário', u'salario'], [u'Qual teu salário? Sou destitute']],
                    [[u'teclado', u'bash', u'shell'], [u'Teclado no bash do android?']],
                    [[u'quebra', u'cadeira', u'mesa'], [u'Precisam de um manutenir?']],
                    [[u'coca', u'refri'], [u'Nossa essa me dói o figado']],
                    [[u'função', u'cargo'], [u'Sou ass monitor pleno 2', u'Sou Higienizador Senior 1', u'Sou Bombona carries junior 3', u'Sou Ethnic Terminator senior 3', u'Sou Linux Software Engineer']],
                    [[u'banco'], [u'Bank of America']],
                    [[u'nestor'], [u'Hi Nestor']],
                    [[u'lesse', u'leu'], [u'Praticamente']],
                    [[u'alemão', u'alemao'], [u'Verschlange', u'Auf deine mutter', u'Schultz']],
                    [[u'jogo', u'jogar'], [u'Jogar um Medal of Honor?']],
                    [[u'pagamento', u'cascalho'], [u'É dia 2?']],
                    [[u'android'], [u'Android usa Linux?']],
                    [[u'selfie'], [u'Eu gosto de pau de selfie']],
                    [[u'estados unidos', u'tio sam'], [u'Prefiro Angola']],
                    [[u'força', u'forte'], [u'Eu uso pulseira de força']],
                    [[u'gord'], [u'Vou fazer uma bariátrica']],
                    [[u'tela'], [u'Screen security?']],
                    [[u'tamanho'], [u'Acho que é GG']],
                    [[u'pobre', u'fudido'], [u'Também sou destitute']],
                    [[u'mst'], [u'Sou presidente do MST, movimento sem trabalho']],
                    [[u'lula', u'pt'], [u'Lula é meu senhor e pinga não me faltará']],
                    [[u'esquecido', u'esqueci'], [u'Pô David toto mundo ja tinha equesido dizo']]
                   ]

many_keywords_speaches = [[], []]

LAST_DAVID_HAIR_CALL = None

def passar_mao_cabelo_david(message, chat_id, com):
    global LAST_DAVID_HAIR_CALL
    if 'from' in message and 'first_name' in message['from'] and 'david' == message['from']['first_name'].lower():
        now = datetime.datetime.now()
        if LAST_DAVID_HAIR_CALL:
            print((now - LAST_DAVID_HAIR_CALL).seconds)
        if LAST_DAVID_HAIR_CALL == None or (now - LAST_DAVID_HAIR_CALL).seconds > 18000:#5 hours
                send_message('Oi David posso passar a mão no seu cabelo?', chat_id, com)
                LAST_DAVID_HAIR_CALL = now

def process_msg(message, text, chat_id, group_title, com):
    passar_mao_cabelo_david(message, chat_id, com)

    text = text.lower()
    for ks in single_keywords_speaches:
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

    t = datetime.datetime.now(tz=pytz.utc)
    #t = t.astimezone(pytz.timezone('America/Sao_Paulo'))
    t = t.astimezone(pytz.timezone('US/Pacific'))
    t = t.replace(hour=9, minute=40)
    com.schedule_every_day_msg(t, 'Ora dos peão mostrar o que fizeram pro capataz', -286666955)

    t = t.astimezone(pytz.timezone('America/Sao_Paulo'))
    t = t.replace(hour=7, minute=55)
    com.schedule_every_day_msg(t, 'Mais um dia de labuta', -286666955)

    t = t.astimezone(pytz.timezone('America/Sao_Paulo'))
    t = t.replace(hour=11, minute=30)
    com.schedule_every_day_msg(t, 'Bora cume?', -286666955)

    t = t.astimezone(pytz.timezone('America/Sao_Paulo'))
    t = t.replace(hour=11, minute=47)
    com.schedule_every_day_msg(t, 'Ai que fome!!!! Minha bariátrica que não chega', -286666955)

    t = t.astimezone(pytz.timezone('America/Sao_Paulo'))
    t = t.replace(hour=11, minute=33)
    com.schedule_every_day_msg(t, 'Hi Nestor', -286666955)

    t = t.astimezone(pytz.timezone('America/Sao_Paulo'))
    t = t.replace(hour=11, minute=56)
    com.schedule_every_day_msg(t, 'Uma coquinha agora ia bem', -286666955)

    t = t.astimezone(pytz.timezone('America/Sao_Paulo'))
    t = t.replace(hour=10, minute=30)
    com.schedule_every_day_msg(t, 'Alguém pode me ajuda cum angular javascript? Sou Linux Software Engineer', -286666955)

    com.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        _exit(0)
