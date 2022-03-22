from time import sleep
import threading

mutex = threading.Lock()
contador = 0

def acesso_buffer(op, thread, buffer):
    global contador 
    mutex.acquire()
    if op == 'Inserir':
        if len(buffer) <= 9:
            contador += 1
            buffer.append(contador)
            print(buffer)
    elif op == 'Consumir':
        try:
            print(f'A {thread} consumiu o número: {buffer.pop(0)}')
            print(buffer)
        except:
            pass
    mutex.release()


def produtora(thread, buffer):
    while True:
        sleep(0.5)
        acesso_buffer('Inserir', thread, buffer)

        if buffer[-1] >= 100:
            break

def consumidora(thread, buffer):
    while True:
        sleep(0.5)
        if len(buffer) > 0:
            if buffer[0] >= 100:
                break
            acesso_buffer('Consumir', thread, buffer)
    
    

buffer = [0]


p1 = threading.Thread(target=produtora, args=('p1', buffer))
p2 = threading.Thread(target=produtora, args=('p1', buffer))

c1 = threading.Thread(target=consumidora, args=('C1', buffer))
c2 = threading.Thread(target=consumidora, args=('C2', buffer))
c3 = threading.Thread(target=consumidora, args=('C3', buffer))

threads = [p1, p2, c1, c2, c3]


for t in threads:
    t.start()

for t in threads:    
    t.join()

print('Finalizado!')
