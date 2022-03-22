#coding=UTF-8
import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 3000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print('>> CHAT SÍNCRONO CLIENTE x SERVIDOR <<')
    client.connect((SERVER, PORT))
    client.send(input('User: ').encode())
    print('Conectado!')
    while True:
        msg = input('Mensagem: ')
        client.send(msg.encode())
        if msg == '':
            break
        # resp = client.recv(1024).decode()
        # print(f'Resposta: {resp}')

    client.close()
except Exception as e: 
    client.close()
    print(e)
    exit()

