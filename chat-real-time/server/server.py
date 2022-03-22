#coding=UTF-8
import socket
from threading import Thread


def handleConnection():
    while True:
        connection, address = SERVER.accept()
        # user = connection.recv(1024).decode('utf-8')
        client = {
            "user": address,
            "address": address}

        clients.append(client)

        t = Thread(target=handleClient, args=(connection, client)).start()

def handleClient(connection, client):
    print(client['user'], client["address"])
    # print(client)
    
    while True:
        data = connection.recv(1024).decode('utf-8')
        if(not data):
            print(f'connection to {client["user"]} closed!')
            connection.close()
            break
        
        print(f'Recebido > {data}')



HOST = socket.gethostbyname(socket.gethostname())
# HOST = 'localhost'
PORT = 3000
SOCKET = (HOST, PORT)

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

SERVER.bind(SOCKET)
print('Servidor Iniciado em {}'.format(SOCKET))

clients = []


if __name__ == "__main__":
    SERVER.listen(5)
    handleConnection()
    # t2= Thread(target= handleConnection)
    # t2.start()
    # t2.join()
    SERVER.close()


