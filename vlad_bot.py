# coding=utf-8

import sys
import time
import pprint
import telepot
import random
import os
import emoji
import re
from collections import deque
from telepot.loop import MessageLoop

filaFera = deque(maxlen=20)
filaDiz = deque(maxlen=5)

#achou que ia roubar o bot? ACHOU ERRADO OTARIO!
TOKEN = os.environ['TELEGRAM_TOKEN']

def handle(msg):
	if 'text' not in msg:
		return	
	chat_id = msg['chat']['id']
	command = msg['text']
	msg_id = msg['message_id']

	if (command.startswith('/')):
		
		pics = [f for f in os.listdir('/app/images/')]
		audios = [f for f in os.listdir('/app/sound/')]

		response = ["Gua", "Beisso aí", "Risos", "Hausha7hausua7e", "Calma", "Te fode carlos", "Nossa", "Você tá bem, cara?", "Uia", "Te fode carlos", ".", "Egua" , "Nao ma", "Bacana", "Essa fera", "Que loucura", "Te fode carlos", "O loco Bichow", "Tenso", "Diz", "Rs", "E foi indo e foi indo... E tamo aqui agora", "Meu nome é Vladimir Lima tenho 24 anos, faço cerveja, ando de bicicleta e só", "Complicado esse humor", "boa", "Esse tempo todo?", "Vai fumar maconha ma\nQue tu fica de boas\nMenos exaltado", "Bebam água"]
		responseAsk = ["Calma, explica aí q eu não entendi", "Q?", "Depende", "Não sei, foda-se", "Que pergunta bosta, em? Vai se fuder", "Não, te fode", "Provavelmente nao em...", "Olha, eu acho que sim em...", "Dificil isso...", "Olha, talvez", "Sim! AEAEAEAEA!", "Peraí que eu to comendo"]

		if command == '/help' or command == '/help@vlademeeer_bot':
			print ('Command ' + command + ' received from chat ' + repr(chat_id) + ' ...')
			bot.sendMessage(chat_id, "*Vlad Bot v4.7*\n\nCara, a minha cabeça é difícil de entender. Da pra explicar não, foi mal. MAAAS, tem uns comandos bacanas aí oh...\n\n*/vlad* - faço um comentário extremamente enriquecedor para a conversa\n\n*/askvlad* - respostas honestas para qualquer pergunta\n\n*/fera* - minhas fotos sensuais que leva todo mundo a loucura\n\n*/calma* - CALMA SENHORA\n\n*/diz* - minha voz inconfundível pra vc se deliciar\n\n\n*Desenvolvido por:* Yuri Reis / Bruno Monteiro", parse_mode='Markdown')
		
		if command == '/calma' or command == '/calma@vlademeeer_bot':
			print ('Command ' + command + ' received from chat ' + repr(chat_id) + ' ...')
			calma = random.randint(0,1);
			if calma == 0:
				print ('Sending calma to chat: ' + repr(chat_id) + ' ...')
				with open('/app/calma.jpg', 'rb') as f:
					bot.sendPhoto(chat_id, f)
				f.close()
			elif calma == 1:
				print ('Sending calma2 to chat: ' + repr(chat_id) + ' ...')
				with open('/app/calma2.jpg', 'rb') as f:
					bot.sendPhoto(chat_id, f)
				f.close()

		if command == '/vlad' or command == '/vlad@vlademeeer_bot':
			print ('Command ' + command + ' received from chat ' + repr(chat_id) + ' ...')
			op = random.choice(response)

			'''while op in filaVlad:
				op = random.choice(response)
			filaVlad.append(op)'''

			print ('Sending ***' + op + '*** to chat: ' + repr(chat_id) + ' ...')
			bot.sendMessage(chat_id, op)
		'''elif '/vlad' in command:
				c, r=command.split(' ', 1)
			if not r.isdigit():
				print (r + ' IS NOT A NUMBER !!!')
				bot.sendMessage(chat_id, "Ma... Eu acho que *" + r.upper() + "* nao eh um numero " + emoji.emojize(":thinking_face:"), parse_mode='Markdown')
			else:
				r = int(r)
				if r < 0 or r > len(response)-1:
					print (repr(r) + ' IS NOT IN RANGE !!!')
					bot.sendMessage(chat_id, "Ei... Éééééé... Tem que tá dentro do intervalo de *[0 até " + repr(len(response)-1) + "]*", parse_mode='Markdown')
				else:
					print ('Sending ' + response[r] + ' to chat: ' + repr(chat_id) + ' ...')
					bot.sendMessage(chat_id, response[r])
		'''

		if command == '/fera' or command == '/fera@vlademeeer_bot':
			print ('Command ' + command + ' received from chat ' + repr(chat_id) + ' ...')
			img = random.choice(pics)
			while img in filaFera:
				img = random.choice(pics)
			filaFera.append(img)

			if (img.endswith('.gif')):
				print ('Sending gif ***' + img + '*** to chat: ' + repr(chat_id) + ' ...')
				with open('/app/images/%s' % img, 'rb') as f:
					bot.sendDocument(chat_id, f)
				f.close()
			else:
				print ('Sending pic ***' + img + '*** to chat: ' + repr(chat_id) + ' ...')
				with open('/app/images/%s' % img, 'rb') as f:
					bot.sendPhoto(chat_id, f)
				f.close()

		'''elif '/fera' in command:
			c, p = command.split(' ', 1)
			if not p.isdigit():
				print (p + ' IS NOT A NUMBER !!!')
				bot.sendMessage(chat_id, "Ma... Eu acho que *" + p.upper() + "* nao eh um numero " + emoji.emojize(":thinking_face:"), parse_mode='Markdown')
			else:
				p = int(p)
				if p < 0 or p > len(pics)-1:
					print (repr(p) + ' IS NOT IN RANGE !!!')
					bot.sendMessage(chat_id, "Ei... Éééééé... Tem que tá dentro do intervalo de *[0 até " + repr(len(pics)-1) + "]*", parse_mode='Markdown')
				else:
					with open('/app/images/%s' % pics[p], 'rb')
					print ('Sending pic ' + pics[p] + ' to chat: ' + repr(chat_id) + ' ...')

					bot.sendPhoto(chat_id, f)
					f.close()
		'''

		if command == '/mito' or command == '/mito@vlademeeer_bot':
			bot.sendMessage(chat_id, 'Opa querido(a), esse comando foi substituído pelo /fera, por motivos de **FASCISMO**, perdão pelo incoveniente', parse_mode='Markdown')

		if command == '/askvlad' or command == '/askvlad@vlademeeer_bot':
			print ('Command ' + command + ' received from chat ' + repr(chat_id) + ' ...')
			bot.sendMessage(chat_id, "Algo de errado não está certo, cadê a pergunta?", reply_to_message_id=msg_id)
		elif '/askvlad' in command:
			print ('Command ' + command + ' received from chat ' + repr(chat_id) + ' ...')
			opAsk = random.choice(responseAsk)
			print ('Sending ***' + opAsk + '*** to chat: ' + repr(chat_id) + ' ...')
			bot.sendMessage(chat_id, opAsk, reply_to_message_id=msg_id)

		if command == '/diz' or command == '/diz@vlademeeer_bot':
			print ('Command ' + command + ' received from chat ' + repr(chat_id) + ' ...')
			aud = random.choice(audios)

			while aud in filaDiz:
				aud = random.choice(audios)
			filaDiz.append(aud)

			print ('Sending audio ***' + aud + '*** to chat: ' + repr(chat_id) + ' ...')
			with open('/app/sound/%s' % aud, 'rb') as f:
				bot.sendVoice(chat_id, f)
			f.close()
			'''elif '/diz' in command:
				c, a = command.split(' ', 1)
				if not a.isdigit():
					print (a + ' IS NOT A NUMBER !!!')
					bot.sendMessage(chat_id, "Ma... Eu acho que *" + a.upper() + "* nao eh um numero " + emoji.emojize(":thinking_face:"), parse_mode='Markdown')
				else:
					a = int(a)
					if a < 0 or a > len(audios)-1:
						print (repr(a) + ' IS NOT IN RANGE !!!')
						bot.sendMessage(chat_id, "Ei... Éééééé... Tem que tá dentro do intervalo de *[0 até " + repr(len(audios)-1) + "]*", parse_mode='Markdown')
					else:
						with open('/app/sound/%s' % audios[a], 'rb')  
						print ('Sending audio ' + audios[a] + ' to chat: ' + repr(chat_id) + ' ...')

						bot.sendVoice(chat_id, f)
						f.close()
			'''
	elif re.search(r'\btop[^ao]*\b', command, flags=re.IGNORECASE):
		print ('Command TOP received from chat ' + repr(chat_id) + ' ...')
		print ('Sending TOPPER to chat: ' + repr(chat_id) + ' ...')
		bot.sendMessage(chat_id, "Não diga top, diga xibata", reply_to_message_id=msg_id)

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running
<<<<<<< HEAD
while 1:
=======
.while 1:
>>>>>>> b49fdf1c7e973b768e5e58d11d9bb7b0ac1a4f7c
	time.sleep(10)