# para executar o código do cliente basta instalar a biblioteca websocket
# -> pip install websockets

from threading import Thread
from server.server import Server
from server.clientWeb import ClientWeb

server = Server()
client = ClientWeb()


t = Thread(target=server.serverStart, ).start()
client.startServer()
server.stopServer()

