import socket
import time
import json

message = {
'chunks': '4',
'ids': [1, 2, 3, 4],
}

downloaded_ids = []

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

#client.settimeout(0.2)

def dict_to_binary(dict_data):
	strin = json.dumps(dict_data).encode('utf-8')
	return strin


client.sendto(dict_to_binary(message), ('<broadcast>', 37020))
print('mensagem enviada')
time.sleep(3)

while len(downloaded_ids) <= len(message['ids']):
	data, addr = client.recvfrom(1024)
	print(data.decode('utf-8'), addr)
	