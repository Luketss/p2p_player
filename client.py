from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
#import protocol iria utilizar TCP, no caso de conexões UDP utilizamos o DatagramProtoco (udp é necessário para enviar)
'''
O protocolo UDP (sigla para User Datagram Protocol) tem, como característica essencial, um atributo que pode parecer esquisito para os iniciantes no tema - a falta de confiabilidade.

Isso significa que, através da utilização desse protocolo, pode-se enviar datagramas de uma máquina à outra, mas sem garantia de que os dados enviados chegarão intactos e na ordem correta.
'''
from random import randint

class Client(DatagramProtocol):
    def __init__(self, host, port):
        if host == 'localhost':
            host = '127.0.0.1'
        #self.id = uuid4()give a random string para usar de ID
        self.id = host, port
        self.address = None
        self.server = '127.0.0.1', 9999
        print('working on id:', self.id)

    def startProtocol(self):
        self.transport.write('ready'.encode('utf-8'), self.server)

    def datagramReceived(self, datagram, addr):
        #datagram é a data recebida e address o remetente
        datagram = datagram.decode('utf-8')
        
        if addr == self.server:
            print('Choose a client\n', datagram)
            self.address = input('write host:'), int(input('Write port'))
            reactor.callInThread(self.send_message)
        else:
            print(addr, ':', datagram)

    def send_message(self):
        while True:
            self.transport.write(input(":::").enconde('utf-8'), self.address)

if __name__ == '__main__':
    port = randint(1000, 5000)
    reactor.listenUDP(port, Client('localhost', port))
    reactor.run()