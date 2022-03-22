import threading
import time

def counter(number, thread, listCont):
  while(listCont[0] < number):
    listCont[0] += 1
    print(f"  {thread}º thread: {listCont[0]}")
    time.sleep(0.5) 


def withThreads():
  start = time.time()

  listCont = [0]
  threads = []

  for t in range(4):
    threads.append(threading.Thread(target=counter, args=(100, t+1, listCont)))
    threads[t].start()
  
  for thread in threads:
    thread.join()
  
  end = time.time()

  print(f'-'*30)
  print(f'->  Com Threads ')
  print(f'  Tarefa realizada em: {end - start:.2f} segundos.')
  print(f'-'*30)


def sequential():
  start = time.time()
  for number in range(1, 101):
    time.sleep(0.5)
  end = time.time() 
  
  print(f'->  Sem Threads <-')
  print(f'  Tarefa realizada em: {end - start:.2f} segundos.')
  print(f'-'*30)


def main():
  withThreads()
  sequential()


main()