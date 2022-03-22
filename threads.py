import threading
import time

RANGE = (10000, 99999)


def verifyPrimeNumber(number):
    for i in range(2, int(number/2) + 1):
      if number % i == 0:
        return False
    return True


def primesNumbers(begin, end, listPrimes):
  primes = []
  cont = 0

  for number in range(begin, end):
    if(verifyPrimeNumber(number)):
      primes.append(number)
      cont += 1

  listPrimes.append(int(cont))


def withThreads(quantityThreads):
  startTime = time.time()
  primes = []
  listPrimes = []

  threads = []
  begin = RANGE[0]
  end = div = int(RANGE[1]/quantityThreads)
  res = (RANGE[1]%quantityThreads)

  for number in range(quantityThreads):
    t = threading.Thread(target=primesNumbers, args=(begin, end, listPrimes))
    threads.append(t)
    t.start()

    begin = end
    end += div
    if(number == quantityThreads-2):
      end += (res+1)


  for t in threads:
    t.join()

  endTime = time.time()

  print(f'-'*20)
  print(f'Utilizando {quantityThreads} Thread')
  print(f'Total de números Primos é: {sum(listPrimes)}')
  print(f'Tarefa realizada em: {endTime - startTime} segundos.')
  print(f'-'*20)


def sequencial():
  listPrimes = []

  startTime = time.time()

  primesNumbers(RANGE[0], RANGE[1]+1, listPrimes)

  endTime = time.time()

  print(f'-'*40)
  print('Programação Sequencial (sem threading)')
  print(f'Total de números Primos é: {sum(listPrimes)}')
  print(f'Tarefa realizada em: {endTime - startTime} segundos.')
  print(f'-'*40)


def main(): 
  sequencial()
  withThreads(2)
  withThreads(4)

main()
