# coding=utf-8

import sys
import time
import pprint
import telepot
import random
import os
from collections import deque

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    filaMito = deque(maxlen=10)
    filaDiz = deque(maxlen=5)
    filaVlad = deque(maxlen=5)

    print ('Command received ... %s', command)

    #LIVE
    pics = [f for f in os.listdir('/var/lib/openshift/573f29582d52714be30000dd/app-root/repo/images/')]
    audios = [f for f in os.listdir('/var/lib/openshift/573f29582d52714be30000dd/app-root/repo/sound/')]

    #DEV
    #pics = [f for f in os.listdir('/Users/yurireis/Documents/vladFlask/myflaskapp/images/')]
    #audios = [f for f in os.listdir('/Users/yurireis/Documents/vladFlask/myflaskapp/sound/')]

    response = ["Risos", "Hausha7hausua7e","Calma","Nossa","Você tá bem, cara?", "Uia", "Te fode carlos", ".", "Egua" , "Nao ma", "Bacana", "Essa fera", "Que loucura", "O loco bichow", "Tenso", "Diz", "Rs", "E foi indo e foi indo... E tamo aqui agora", "Meu nome é Vladimir Lima tenho 24 anos, faço cerveja, ando de bicicleta e só", "Complicado esse humor", "boa", "Esse tempo todo?", "Vai fumar maconha ma\nQue tu fica de boas\nMenos exaltado"]
    responseAsk = ["Não sei, foda-se", "Que pergunta bosta, em? Vai se fuder", "Não, te fode", "Provavelmente nao em...", "Olha, eu acho que sim em...", "Dificil isso...", "Olha, talvez", "Sim! AEAEAEAEA!"]
    
    if command == '/help' or command == '/help@vlademeeer_bot':
    	bot.sendMessage(chat_id, "Vlad Bot v3.1\n\nBicho, a minha cabeça é difícil de entender. Da pra explicar não, foi mal. MAAAS, tem uns comandos bacanas aí oh...\n\n/vlad - faço um comentário extremamente enriquecedor para a conversa\n/askvlad - respostas honestas para qualquer pergunta\n/mito - minhas fotos sensuais que levam até homens a loucura\n/calma - CALMA SENHORA\n/diz - minha voz inconfundível pra vc se deliciar\n\n\nDeveloped by: Yuri Reis / Bruno Monteiro (Só fez um IF.. HEAUDHSADSDSDCVVFLFLFFL te amo cara)")
    if command == '/calma' or command == '/calma@vlademeeer_bot':
        print ('Sending calma ...')
        f = open('/var/lib/openshift/573f29582d52714be30000dd/app-root/repo/calma.jpg', 'rb') 
        bot.sendPhoto(chat_id, f)
    if command == '/vlad' or command == '/vlad@vlademeeer_bot':
        op = random.randint(0,len(response));

        while op in filaVlad:
            op = random.randint(0,len(response))
        filaVlad.append(op)
        
        print ('Sending msg ...')
    	bot.sendMessage(chat_id, response[op])
    if command == '/mito' or command == '/mito@vlademeeer_bot':
        img = random.randint(0,len(pics));
        
        while img in filaMito:
            img = random.randint(0,len(pics));
        filaMito.append(img)

        #LIVE
        f = open('/var/lib/openshift/573f29582d52714be30000dd/app-root/repo/images/%s' % pics[img], 'rb')

        #DEV
        #print ('Sending photo ... %s', pics[img])
        #f = open('/Users/yurireis/Documents/vladFlask/myflaskapp/images/%s' % pics[img], 'rb')

        bot.sendPhoto(chat_id, f)
        f.close()

    if command == '/askvlad' or command == '/askvlad@vlademeeer_bot':
        bot.sendMessage(chat_id, "Algo de errado não está certo, cadê a pergunta?")
    elif '/askvlad' in command:
        opAsk = random.randint(0,len(responseAsk));
        print ('Sending answer ...')
        bot.sendMessage(chat_id, responseAsk[opAsk])
    if command == '/diz' or command == '/diz@vlademeeer_bot':
        aud = random.randint(0,len(audios))

        while aud in filaDiz:
            aud = random.randint(0,len(audios))
        filaDiz.append(aud)

        #LIVE
        f = open('/var/lib/openshift/573f29582d52714be30000dd/app-root/repo/sound/%s' % audios[aud], 'rb')  

        #DEV
        #print ('Sending audio ... %s', audios[aud])
        #f = open('/Users/yurireis/Documents/vladFlask/myflaskapp/sound/%s' % audios[aud], 'rb') 

        bot.sendVoice(chat_id, f)
        f.close()


#LIVE BOT
TOKEN = "220404785:AAHPsh6G845YNKpeexlaF2_-0TC-z4WSwJg"

#DEV BOT
#TOKEN = "397302315:AAGmbVIAyVvAquar8qkA7M6cP1USCEiQO28"

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
    #chupa minha rola yuri
