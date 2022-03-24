## para o funcionamento código do basta instalar a biblioteca websocket
import asyncio
import websockets
import socket
import webbrowser
from threading import Thread
from pathlib import Path


class ClientWeb():
    # websockets
    HOST = 'localhost'
    PORT = 3333

    # Server
    SERVER_PORT = 3000


    def __init__(self, host=HOST, port=PORT):
        self.start_server = websockets.serve(self.handler, host, port)
        self.connected = set()


    def startServer(self):
        asyncio.get_event_loop().run_until_complete(self.start_server)
        fpath = Path('public/login.html').absolute()
        webbrowser.open_new(str(fpath))  
        asyncio.get_event_loop().run_forever()


    def handlerServerConnection(self, port, websocket):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server = socket.gethostbyname(socket.gethostname())
        client.connect((server, port))
        Thread(target=self.receivedMessage, args=(client, websocket)).start()
        return client


    def receivedMessage(self, client, websocket):
        loop = asyncio.new_event_loop()
        loop = asyncio.set_event_loop(loop)

        while True:
            try:
                resp = client.recv(1024).decode()
                if(not websocket in self.connected):
                    continue
                asyncio.get_event_loop().run_until_complete(self.sendMessage(websocket, resp))
            except Exception:
                client.close()
                break


    async def sendMessage(self, websocket, message):
        try:
            await websocket.send(message)
        except:
            self.connected.remove(websocket)
            print('error')
            

    async def handler(self, websocket, path):
        try:
            client = self.handlerServerConnection(ClientWeb.SERVER_PORT, websocket)
            self.connected.add(websocket)

            async for message in websocket:
                client.send(message.encode())

        finally:
            self.connected.remove(websocket)
            close = 'close' 
            client.send(close.encode())


if __name__ == "__main__":
    clientServer = ClientWeb()
    clientServer.startServer()



 
