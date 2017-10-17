# coding=utf-8

import sys
import time
import pprint
import telepot
import random
import os
from collections import deque

filaMito = deque(maxlen=20)
filaDiz = deque(maxlen=5)
filaVlad = deque(maxlen=5)

TOKEN = os.environ['TELEGRAM_TOKEN']

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Command ' + command.encode('utf-8') + ' received ...')

    #LIVE
    pics = [f for f in os.listdir('/app/images/')]
    audios = [f for f in os.listdir('/app/sound/')]

    response = ["Gua", "Beisso aí","Risos", "Hausha7hausua7e", "Calma", "Nossa", "Você tá bem, cara?", "Uia", "Te fode carlos", ".", "Egua" , "Nao ma", "Bacana", "Essa fera", "Que loucura", "O loco bichow", "Tenso", "Diz", "Rs", "E foi indo e foi indo... E tamo aqui agora", "Meu nome é Vladimir Lima tenho 24 anos, faço cerveja, ando de bicicleta e só", "Complicado esse humor", "boa", "Esse tempo todo?", "Vai fumar maconha ma\nQue tu fica de boas\nMenos exaltado"]
    responseAsk = ["Calma, explica aí q eu não entendi", "Q?", "Depende", "Não sei, foda-se", "Que pergunta bosta, em? Vai se fuder", "Não, te fode", "Provavelmente nao em...", "Olha, eu acho que sim em...", "Dificil isso...", "Olha, talvez", "Sim! AEAEAEAEA!", "Peraí que eu to comendo"]

    if command == '/help' or command == '/help@vlademeeer_bot':
        bot.sendMessage(chat_id, "*Vlad Bot v3.5*\n\nBicho, a minha cabeça é difícil de entender. Da pra explicar não, foi mal. MAAAS, tem uns comandos bacanas aí oh...\n\n*/vlad* - `faço um comentário extremamente enriquecedor para a conversa`\n*/askvlad* - `respostas honestas para qualquer pergunta`\n*/mito* - `minhas fotos sensuais que levam até homens a loucura`\n*/calma* - `CALMA SENHORA`\n*/diz* - `minha voz inconfundível pra vc se deliciar`\n\n\n*Developed by:* `Yuri Reis / Bruno Monteiro`", parse_mode='Markdown')
    
    if command == '/calma' or command == '/calma@vlademeeer_bot':
        calma = random.randint(0,1);
        if calma == 0:
            print ('Sending calma to chat: ' + repr(chat_id) + ' ...')
            f = open('/app/calma.jpg', 'rb') 
            bot.sendPhoto(chat_id, f)
        elif calma == 1:
            print ('Sending calma2 to chat: ' + repr(chat_id) + ' ...')
            f = open('/app/calma2.jpg', 'rb') 
            bot.sendPhoto(chat_id, f)

    if command == '/vlad' or command == '/vlad@vlademeeer_bot':
        op = random.randint(0,len(response)-1);

        while op in filaVlad:
            op = random.randint(0,len(response)-1)
        filaVlad.append(op)

        print ('Sending ' + response[op] + ' to chat: ' + repr(chat_id) + ' ...')
        bot.sendMessage(chat_id, response[op])

    if command == '/mito' or command == '/mito@vlademeeer_bot':
        img = random.randint(0,len(pics)-1);

        while img in filaMito:
            img = random.randint(0,len(pics)-1);
        filaMito.append(img)

        f = open('/app/images/%s' % pics[img], 'rb')
        print ('Sending pic ' + pics[img] + ' to chat: ' + repr(chat_id) + ' ...')

        bot.sendPhoto(chat_id, f)
        f.close()

    if command == '/askvlad' or command == '/askvlad@vlademeeer_bot':
        bot.sendMessage(chat_id, "Algo de errado não está certo, cadê a pergunta?")
    elif '/askvlad' in command:
        opAsk = random.randint(0,len(responseAsk)-1);
        print ('Sending ' + responseAsk[opAsk] + ' to chat: ' + repr(chat_id) + ' ...')
        bot.sendMessage(chat_id, responseAsk[opAsk])

    if command == '/diz' or command == '/diz@vlademeeer_bot':
        aud = random.randint(0,len(audios)-1)

        while aud in filaDiz:
            aud = random.randint(0,len(audios)-1)
        filaDiz.append(aud)

        f = open('/app/sound/%s' % audios[aud], 'rb')  
        print ('Sending audio ' + audios[aud] + ' to chat: ' + repr(chat_id) + ' ...')

        bot.sendVoice(chat_id, f)
        f.close()

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
    #chupa minha rola yuri aeaeae
