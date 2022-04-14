from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
name = MPI.Get_processor_name()
size = comm.Get_size()


def verifyPrimeNumber(number):
    for i in range(2, int(number/2) + 1):
      if number % i == 0:
        return False
    return True


def primesNumbers(begin, end):
  cont = 0
  for number in range(begin, end):
    if(verifyPrimeNumber(number)):
      cont += 1
  return cont


if rank == 0:
  data = [
    {"star": 10000, 'end': 24999}, 
    {"star": 24999, 'end': 49998}, 
    {"star": 49998, 'end': 74997}, 
    {"star": 74997, 'end': 99999}  
  ]

else:
  data = None
  dados = None


data = comm.scatter(data, root=0)
data = primesNumbers(data["star"], data["end"])
print(f'Rank: {rank} Contou:' , data)

dados = comm.gather(data, root=0)
if dados:
  print(f'Total de números Primos: ' , sum(dados))