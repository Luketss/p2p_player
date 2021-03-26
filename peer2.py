import socket
import json

peer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

peer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
peer.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

peer.bind(("", 37020))

avaliable = [1, 2]

def treat_msg(data, addr):
	data = data.decode('utf-8')
	data_dict = json.loads(data)
	for id in data_dict['ids']:
		for value in avaliable:
			if id == value:
				message = f'{id} disponível'
				print(f'{id} disponível no {addr}')
				peer.sendto(message.encode('utf-8'), addr)
	print(f'a mensagem recebida foi: {data}')

print('waiting msg')
while True:
	data, addr = peer.recvfrom(1024)
	treat_msg(data, addr)