#coding=UTF-8
import threading
import time

cont = 0
mutex = threading.Lock()

def contar():
    global cont
    while (cont<100):
        print('Thread {} em execução.'.format(threading.current_thread().name))
        mutex.acquire()  #início da seção crítica
        if(cont<100):
            cont += 1
            time.sleep(0.1)
            print('Thread {} contando: '.format(threading.current_thread().name),cont)
        mutex.release()  #fim da seção crítica


t1 = threading.Thread(target=contar,)
t2 = threading.Thread(target=contar,)
t3 = threading.Thread(target=contar,)

threads = []
threads.append(t1)
threads.append(t2)
threads.append(t3)

for t in threads:
    t.start()
    
for t in threads:    
    t.join()

print('Finalizado!')