#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from communication import Communication, send_message
from time import sleep
from os import _exit

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
                    [[u'pobre', u'fudido'], [u'Também sou destitute']]
                   ]

many_keywords_speaches = [[], []]

def process_msg(text, chat_id, group_title, com):
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
    com.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        _exit(0)
