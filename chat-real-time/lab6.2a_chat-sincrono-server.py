#coding=UTF-8
import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 3000
SOCKET = (SERVER,PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(SOCKET)
server.listen()
print('Servidor Iniciado em {}'.format(SOCKET))

while True:
    conn, addr = server.accept()

    while True:
        msg = conn.recv(1024).decode()
        if msg == '':
            break
        print(f'Recebido > {msg}')
        resp = input('Resposta > ')
        conn.send(resp.encode())
    print(f'Cliente {addr} encerrado.')
    conn.close()