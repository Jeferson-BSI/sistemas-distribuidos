#coding=UTF-8
import socket
from threading import Thread


class Server():
    # HOST = 'localhost'
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 3000
    
    def __init__(self, port=PORT, host=HOST):
        print(Server.PORT, Server.HOST)
        self.socket = (host, port)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(self.socket)
        self.clients = []


    def serverStart(self):
        self.server.listen(5)
        print(f'Server running in port: {Server.HOST}:{Server.PORT}')
        self.handleConnection()


    def serverStop():
        self.server.close()


    def handleConnection(self):
        while True:
            connection, address = self.server.accept()
            user = connection.recv(1024).decode('utf-8')
            client = {
                "user": user,
                "address": address}
            self.clients.append(client)
            print(client['user'], client["address"])

            t = Thread(target=self.handleClient, args=(connection)).start()
        self.serverStop()


    def handleClient(self, connection):
        while True:
            data = connection.recv(1024).decode('utf-8')
            if(not data):
                print(f'connection to {client["user"]} closed!')
                connection.close()
                break
            
            print(f'Received > {data}')


if __name__ == "__main__":
    server = Server()
    server.serverStart()
    server.close()


