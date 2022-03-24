import socket
from threading import Thread
import json


class Server():
    # HOST = 'localhost'
    HOST = socket.gethostbyname(socket.gethostname())
    PORT = 3000
    
    def __init__(self, port=PORT, host=HOST):
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
            if(not user):
                connection.close()
                continue
            try:
                self.broadcast(json.loads(user), connection, self.clients)
                client = {
                    "connection": connection,
                    "user": json.loads(user),
                    "address": address
                    }
                self.clients.append(client)
                t = Thread(target=self.handleClient, args=(connection, client)).start()
            except:
                pass


    def handleClient(self, connection, client):
        while True:
            try:
                data = connection.recv(1024).decode('utf-8')
                
                if(not data):
                    print(f'connection to {client["user"]} closed!')
                    connection.close()
                    self.clients.remove(client)
                    break

                if (data == 'close'):
                    client['user']["message"] = 'close'
                    data = dict(client['user'])
                    
                    self.broadcast(data, connection, self.clients)
                    self.clients.remove(client)
                    break

                self.broadcast(json.loads(data), connection, self.clients)
            except:
                print(f'connection to {client["user"]} closed!')
                connection.close()
                self.clients.remove(client)
                break
            

    def broadcast(self, data, connection, clients):
        for client in clients:
            if client["connection"] != connection:
                if client['user']["chat"] == data["chat"]: 
                    try:
                        client["connection"].send(json.dumps(data).encode())
                    except:
                        client["connection"].close()
                        clients.remove(client)
       

if __name__ == "__main__":
    server = Server()
    server.serverStart()
    server.serverStop()


