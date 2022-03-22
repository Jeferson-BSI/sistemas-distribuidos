import threading
import time


cont = 0
mutex = threading.Lock()


def handleBuffer(thread, option, buffer):
  global cont

  mutex.acquire()
  
  if(option == 'push' and len(buffer) < 10):
    cont += 1
    buffer.append(cont)

  elif (option == 'pop' and len(buffer) > 0):

    print(f"  {thread}: {buffer.pop(0)}")

  mutex.release()  
    

def producer(thread, buffer): 
    while(1):
      time.sleep(0.5)
      handleBuffer(thread, 'push', buffer)

      if(buffer[-1] >= 100):
        break


def consumer(thread, buffer):
  while(1):
    time.sleep(0.5)
    if len(buffer) > 0:
      if (buffer[-1] > 100):
        break
      handleBuffer(thread, 'pop', buffer)


def threads():
  start = time.time()

  buffer = [0] 

  p1 = threading.Thread(target=producer, args=('p1', buffer ))
  p2 = threading.Thread(target=producer, args=('p2', buffer))

  c1 = threading.Thread(target=consumer, args=('c1', buffer))
  c2 = threading.Thread(target=consumer, args=('c2', buffer))
  c3 = threading.Thread(target=consumer, args=('c3', buffer))

  threads = [p1, p2, c1, c2, c3]
  for thread in threads:
    thread.start()
  
  for thread in threads:
    thread.join()
  
  end = time.time()

  print(f'-'*30)
  print(f'  -> Threads ')
  print(f'  Tarefa realizada em: {end - start:.2f} segundos.')
  print(f'-'*30)


def main():
  threads()


main()