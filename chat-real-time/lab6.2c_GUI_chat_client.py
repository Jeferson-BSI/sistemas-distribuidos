#coding=UTF-8
import socket
import threading
import time

from tkinter import *
#sudo apt-get install python3-tk

class Cliente():

    def __init__(self):
        self.clienteSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.autenticado = 0
        self.janelaEntrada = Tk()
        self.constroiJanelaEntrada(self.janelaEntrada)
        if(self.autenticado):
            self.janelaChat = Tk()
            self.constroiJanelaChat(self.janelaChat)        

    def constroiJanelaEntrada(self, entrada):
        entrada.title('Entrar no Chat')
        labelNome = Label(entrada, text='Nome: ')
        labelNome.grid(column=0, row=0, padx=10)
        self.inputNome = Text(entrada, height=1, width=30)
        self.inputNome.grid(column=1, row=0)
        labelServer = Label(entrada, text='Servidor: ')
        labelServer.grid(column=0, row=1, padx=10)
        self.inputServer = Text(entrada, height=1, width=30)
        self.inputServer.grid(column=1, row=1, pady=10, padx=10)
        labelPorta = Label(entrada, text='Porta: ')
        labelPorta.grid(column=0, row=2, padx=10)
        self.inputPorta = Text(entrada, height=1, width=30)
        self.inputPorta.grid(column=1, row=2)

        botao = Button(entrada, text='Entrar', command=self.entrarChat)
        botao.grid(column=1, row=4, padx=20, pady=20)

        entrada.mainloop()
 
    def entrarChat(self):
        self.nome = self.inputNome.get('1.0','end').strip()
        print(self.nome)
        self.server = self.inputServer.get('1.0','end').strip()
        print(self.server)
        self.port = self.inputPorta.get('1.0','end').strip()
        print(self.port)
        try:
            SOCKET = (f'{self.server}',int(self.port))
            self.clienteSock.connect(SOCKET)
            self.autenticado = 1
            self.janelaEntrada.destroy()
        except Exception as e:
            print(e)

    def constroiJanelaChat(self, janela):
        janela.title('Meu Chat')

        chat = Text(janela)
        chat.grid(column=0, row=0, padx=20, pady=10)
        chat.insert('end',f'Seja Bem Vindo: {self.nome}\n')

        texto = Text(janela, height=2)
        texto.grid(column=0, row=1, padx=20, pady=10)

        botao = Button(janela, text='Enviar')
        botao.grid(column=0, row=2, padx=20, pady=10)

        janela.mainloop()
        print('Janela Principal Construida!')

cli = Cliente()