#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from communication import Communication, send_message
from time import sleep
from os import _exit
import datetime, pytz

GROUP_CHAT_ID = -271497936

single_keywords_speaches = [
    [[u"indian"], [u"Acredito que se trata de um povo inteligente e dedicado em extrema ascenção que em poucas décadas provavelmente estará no top 3 países mais ricos do mundo."]],
    [[u"vida"], [u"Sou um matuto sofrido"]],
    [[u'foda', u'dific', u'difíc', u'sofri', u'sofre', u'sofrê'], [u"Quando eu era um matutinho tive q trabaia pra compra meu primeiro computador."]],
    [[u'$', u'dólar', u'dolar', u'dollar'], [u'Aaahh U$1,00 é tudo que eu queria.']],
    [[u'balde'], [u'Me chamaram?']],
    [[u'merda'], [u'Alguém precisando de um balde?']],
    [[u'chulé', u'chule'], [u'Não fui eu']],
    [[u'linguagem', u'linguagens', u'java', u'javascript', u'delphi', u'python', u'node', u'sql'], [u'Eu programo em AngularJS']],
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
    [[u'peru', u'perú'], [u'Eu queria dois perus, um pra comer e o outro pra ...']],
    [[u'piroca'], [u'Prefiro pau de selfie']],
    [[u'kernel'], [u'Marcos o kernel é escrito em Angular?']],
    [[u'genco'], [u'cloroquina', u'Acessem http://www.genco.com.br/ e conheçam nossa linha de algicidas.', u'Bati a meta e agora vou dobrá-la.', u'https://www.youtube.com/watch?v=e1BJDJIZ3hM&feature=emb_logo', u'https://www.youtube.com/watch?v=S8Z77AtlGFQ&feature=emb_logo']],
    [[u'dudu', u'gigi'], [u'https://www.youtube.com/watch?v=5Q3zsH4nf2s&feature=emb_logo']],
    [[u'cloro', u'piscina'], [u'Você conhece os produtos genco? Acesse https://www.genco.com.br e conheça nossa linha de podrutos']],
    [[u'angola'], [u'Programei SQL e Angular na Angola']],
    [[u'cesta'], [u'Eu prefiro cesta básica a ganhar um peru']],
    [[u'shared', u'memory'], [u'shared memory usa ponteiro?', u'O kernel tem shared memory?']],
    [[u'ponteiro'], [u'@mpdesouza tem curso de ponteiro na udemy?', u'Edson, o que é um ponteiro???']],
    [[u'computador'], [u'Tive que trabaia pa compra meu primeiro coputador']],
    [[u'edson'], [u'Edson, me ajuda numas shared memory??']],
    [[u'manager'], [u'ouvi um cross blowjob??']],
    [[u'sogra'], [u'olha, agora eu virei amigo da minha sogra.']],
    [[u'carro'], [u'é dificil manter um corola']],
    [[u'russa'], [u'to fazendo roleta russa com as contas esse mes.']]
]

#LAST_DIETA_BAMBAM_CALL = None

def send_message_command(message, text, chat_id, com):
    try:
        text.index('send_msg')
        parts_command = text.split(';')
        if len(parts_command) == 3:
            destination_chat_id = parts_command[1].strip()
            msg = parts_command[2].strip()
            send_message(msg, destination_chat_id, com)
            return True
    except:#if no send_msg is found on text an exception will occur, in this case just return False meaning the command was not executed
        None
    return False

"""
def dieta_bambam(message, chat_id, com):
    global LAST_DIETA_BAMBAM_CALL
    if 'from' in message and 'first_name' in message['from'] and 'guilherme' == message['from']['first_name'].lower():
        now = datetime.datetime.now()
        if LAST_DIETA_BAMBAM_CALL == None or (now - LAST_DIETA_BAMBAM_CALL).seconds > 18000:#5 hours
                send_message('O Bambam me passa a tua dieta ai!', chat_id, com)
                LAST_DIETA_BAMBAM_CALL = now
                return True
    return False
"""

def process_msg(message, text, chat_id, group_title, com):
    if (send_message_command(message, text, chat_id, com)):
        #dieta_bambam(message, chat_id, com)):
        return

    text = text.lower()
    for ks in single_keywords_speaches:
        for keyword in ks[0]:
            if keyword in text:
                index = 0
                if len(ks[1]) > 1:
                    index = randint(0, len(ks[1]) - 1)
                print("enviando resposta {}".format(ks[1][index]))
                send_message(ks[1][index], chat_id, com)
                break

if __name__ == '__main__':
    com = Communication()
    com.on_receive_msg(process_msg)

    """
    t = datetime.datetime.now(tz=pytz.utc)
    t = t.astimezone(pytz.timezone('US/Pacific'))
    t = t.replace(hour=9, minute=55)
    com.schedule_every_day_msg(t, 'Como vai o mitin? Muita fulerage?', GROUP_CHAT_ID)

    t = t.astimezone(pytz.timezone('America/Sao_Paulo'))
    t = t.replace(hour=11, minute=56)
    com.schedule_every_day_msg(t, 'Uma coquinha agora ia bem', GROUP_CHAT_ID)
    """

    com.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        _exit(0)
