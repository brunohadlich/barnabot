#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from communication import Communication, send_message
from time import sleep
from os import _exit
import datetime, pytz

GROUP_CHAT_ID = -271497936

single_keywords_speaches = [
    [[u"vida"], [u"A vida (do termo latino vita) é um conceito muito amplo e admite diversas definições. Pode-se referirː ao processo em curso do qual os seres vivos são uma parte; ao espaço de tempo entre a concepção e a morte de um organismo; à condição de uma entidade que nasceu e ainda não morreu; e àquilo que faz com que um ser esteja vivo. Metafisicamente, a vida é um processo contínuo de relacionamentos."]],
    [[u'foda', u'dific', u'difíc', u'sofri', u'sofre', u'sofrê'], [u"O sofrimento e a dificuldade são etapas intrinsicas a vida e que são necessárias para nos fazer crescer como individuo.."]],
    [[u'$', u'dólar', u'dolar', u'dollar'], [u'O dólar americano é a moeda utilizada pelos país Estados Unidos.']],
    [[u'balde'], [u'O balde é um objeto geralmente composto de plastico com o intuito de poder armazenar liquidos mas que pode vir a ser utilizado para outros propósitos.']],
    [[u'merda'], [u'Vamos manter a classe por favor, palavras de baixo calão não ajudam em nada.']],
    [[u'chulé', u'chule'], [u'Chulé não é bom, favor utilizar pé de atleta.']],
    [[u'java', u'javascript', u'delphi', u'python', u'node', u'sql'], [u'Gosto dessa linguagem']],
    [[u'caro'], [u'Você sabia? pessoas que são muito pobres nos EUA são chamadas de destitute']],
    [[u'salário', u'salario'], [u'O salário é algo pessoal e que deve ser compartilhado apenas por desejo particular e não pelo interesse alheio.']],
    [[u'teclado'], [u'Você quis dizer teclado mecânico?']],
    [[u'bash', u'shell'], [u'O bash(born again shell) é um tipo de shell.']],
    [[u'quebra', u'cadeira', u'mesa'], [u'Entrem em contato com uma loja especializada no reparo de mesas e cadeiras.']],
    [[u'coca', u'refri'], [u'Coca é um refrigerante com alto teor de açucar e prejudicial a saúde.']],
    [[u'função', u'cargo'], [u'Sou Software Engineer']],
    [[u'banco'], [u'Bank of America é um cliente em potencial para a ZPE.']],
    [[u'nestor'], [u'Nestor é um ótimo colega de trabalho, sempre disposto a ajudar o restante do grupo.']],
    [[u'lesse', u'leu'], [u'A leitura muda vidas.']],
    [[u'alemão', u'alemao'], [u'No passado fiz muitas piadas com o povo alemão mas hoje sou outra pessoa.']],
    [[u'jogo', u'jogar'], [u'O que você(s) gostaria(m) de jogar?']],
    [[u'pagamento', u'cascalho'], [u'O salário deve cair na conta até o quinto dia util do mês.']],
    [[u'android'], [u'Android é um sistema operacional baseado em linux com foco em dispositivos móveis.']],
    [[u'selfie'], [u'Selfies se tornaram muito comuns com o advento dos smartphones.']],
    [[u'estados unidos', u'tio sam'], [u'Já estive nos Estados Unidos']],
    [[u'força', u'forte'], [u'Para aumentar a força faça atividades fisicas.']],
    [[u'gord'], [u'Ser obeso é prejudicial a saúde.', u'Gordo é um termo prejorativo use Obeso']],
    [[u'tela'], [u' Espiar a tela dos outros não é nada legal']],
    [[u'tamanho'], [u'Depende da sua idade e peso.']],
    [[u'pobre', u'fudido'], [u'Já fui um dia']],
    [[u'mst'], [u'MST significa movimento sem terra']],
    [[u'lula', u'pt'], [u'Lula é um ex-presidente brasileiro que agora se encontra preso por corrupção.']],
    [[u'peru', u'perú'], [u'Peru é uma ave muito saborosa']],
    [[u'piroca'], [u'Olha o palavreado']],
    [[u'kernel'], [u'Kernel é uma palavra utilizada em computação para definir o núcleo de um sistema operacional']],
    [[u'esquecido', u'esqueci'], [u'Esquecimento pode significar amnésia ou uma doença mais perigosa que deve ser verificada por um médico.']],
    [[u'vim'], [u'Eu escutei VIM? que tal uma dica? Imagine que você esta análisando um arquivo de log e gostaria de destacar todas as vezes que a palavra `ERROR` aparece. Você pode fazer o seguinte: :match ErrorString /ERROR/']],
    [[u'salsicha', u'criptografia'], [u'Trata-se de um conjunto de regras que visa codificar a informação de forma que só o emissor e o receptor consiga decifrá-la']],
    [[u'firewall'], [u'Firewall é uma solução de segurança baseada em hardware ou software (mais comum) que, a partir de um conjunto de regras ou instruções, analisa o tráfego de rede para determinar quais operações de transmissão ou recepção de dados podem ser executadas.']],
    [[u'olá'], [u'Oi eu sou o Barnabot_2019 um bot desenvolvido para promover um ambiente saúdavel e feliz neste grupo']],
    [[u'cleito'], [u'Olha a pedraaaa! Dança reggero!']],
    [[u'ana julia', u'ana júlia'], [u'Você quis dizer Juliana certo?']],
    [[u'genco', u'gencopet', u'genco boy'], [u'Iniciamos nossas atividades em 1973 com projeto de produzir tintas, vernizes e adesivos (dai o nome “GENeral COatings” - revestimentos gerais, em inglês), o que logo se provou impraticável. Para continuar com a empresa em operação, valemo-nos de uma matéria prima usada em tintas e formulamos nosso primeiro produto comercial: GENPOOL-X, Algicida e Algistático para piscinas. Naquela época o único produto utilizado para controlar algas em piscinas era o sulfato de cobre.']],
    [[u't800', u'T800', u't-800', u't 800'], [u'T-800 foi enviado pela Skynet para 1984 com a intenção de matar Sarah Connor, antes dessa dar à luz o futuro líder da resistência humana contra as máquinas, John Connor. Mas os humanos invadiram a instalação da máquina do tempo e ao verem que um robô já tinha sido enviado, enviaram um soldado, Kyle Reese, para proteger Sarah.']],
    [[u'india', u'indiano', u'indianos'], [u'Relativo ou pertencente à Índia, país asiático.']],
    [[u'erva'], [u'Aqui na firma temos chá de capim, gostoso e nutritivo.']],
    [[u'droga'], [u'Fiz proerd então sou contra o uso de tóxicos.']],
    [[u'ramid'], [u'Do you wat to try my cookie cookie? only 99 cents plus tax (Michael do the office sobre Ramid)']]
]

LAST_DAVID_HAIR_CALL = None
LAST_DIETA_BAMBAM_CALL = None
LAST_JOSIAS_API_CALL = None

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

#def passar_mao_cabelo_david(message, chat_id, com):
#    global LAST_DAVID_HAIR_CALL
#    if 'from' in message and 'first_name' in message['from'] and 'david' == message['from']['first_name'].lower():
#        now = datetime.datetime.now()
#        if LAST_DAVID_HAIR_CALL == None or (now - LAST_DAVID_HAIR_CALL).seconds > 18000:#5 hours
#                send_message('Oi David posso passar a mão no seu cabelo?', chat_id, com)
#                LAST_DAVID_HAIR_CALL = now
#                return True
#    return False

#def dieta_bambam(message, chat_id, com):
#    global LAST_DIETA_BAMBAM_CALL
#    if 'from' in message and 'first_name' in message['from'] and 'guilherme' == message['from']['first_name'].lower():
#        now = datetime.datetime.now()
#        if LAST_DIETA_BAMBAM_CALL == None or (now - LAST_DIETA_BAMBAM_CALL).seconds > 18000:#5 hours
#                send_message('O Bambam me passa a tua dieta ai!', chat_id, com)
#                LAST_DIETA_BAMBAM_CALL = now
#                return True
#    return False

#def josias_api(message, chat_id, com):
#    global LAST_JOSIAS_API_CALL
#    if 'from' in message and 'first_name' in message['from'] and 'josias' == message['from']['first_name'].lower():
#        now = datetime.datetime.now()
#        if LAST_JOSIAS_API_CALL == None or (now - LAST_JOSIAS_API_CALL).seconds > 18000:#5 hours
#                messages = ['Josias já acabou a API?', 'Josias quer ajuda pra criar uma VM?']
#                send_message(messages[randint(0, len(messages) - 1)], chat_id, com)
#                LAST_JOSIAS_API_CALL = now
#                return True
#    return False

def process_msg(message, text, chat_id, group_title, com):
#    if (send_message_command(message, text, chat_id, com) or
    if (send_message_command(message, text, chat_id, com)):
#        passar_mao_cabelo_david(message, chat_id, com) or
#        dieta_bambam(message, chat_id, com) or
#        josias_api(message, chat_id, com)):
        return

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

#    t = datetime.datetime.now(tz=pytz.utc)
#    t = t.astimezone(pytz.timezone('US/Pacific'))
#    t = t.replace(hour=9, minute=55)
#    com.schedule_every_day_msg(t, 'Ora do mitim peçoal', GROUP_CHAT_ID)

#    t = t.astimezone(pytz.timezone('US/Pacific'))
#    t = t.replace(hour=10, minute=10)
#    com.schedule_every_day_msg(t, 'Como vai o mitin? Muita fulerage?', GROUP_CHAT_ID)

#    t = t.astimezone(pytz.timezone('America/Sao_Paulo'))
#    t = t.replace(hour=7, minute=55)
#    com.schedule_every_day_msg(t, 'Mais um dia de labuta', GROUP_CHAT_ID)

#    t = t.astimezone(pytz.timezone('America/Sao_Paulo'))
#    t = t.replace(hour=11, minute=30)
#    com.schedule_every_day_msg(t, 'Bora cume?', GROUP_CHAT_ID)

#    t = t.astimezone(pytz.timezone('America/Sao_Paulo'))
#    t = t.replace(hour=11, minute=47)
#    com.schedule_every_day_msg(t, 'Ai que fome!!!! Minha bariátrica que não chega', GROUP_CHAT_ID)

#    t = t.astimezone(pytz.timezone('America/Sao_Paulo'))
#    t = t.replace(hour=11, minute=56)
#    com.schedule_every_day_msg(t, 'Uma coquinha agora ia bem', GROUP_CHAT_ID)

    com.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        _exit(0)
