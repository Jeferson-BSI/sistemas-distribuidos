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

# primos = None

if rank == 0:
  data = [
    {"star": 10000, 'end': 24999}, 
  {"star": 24999, 'end': 49998}, 
  {"star": 49998, 'end': 74997}, 
  {"star": 74997, 'end': 99999}  ]

  # for r in range(size):
  #   req = comm.isend(data[r], dest=r, tag=1)
  #   req.wait()
  

  # total = 0
  # for r in range(size):
  #   req = comm.irecv(source=r, tag=1)
  #   primos = req.wait()
  #   print(primos)
  #   total += primos

  # print(f"Total: {total}")

else:
  # req = comm.irecv(source=0, tag=1)
  # data = req.wait()

  # primos = primesNumbers(data["star"], data["end"])
  # req = comm.isend(primos, dest=0, tag=1)
  # print(data)


# total = None
  # print(primos)
  # req = comm.isend(primos, dest=0, tag=2)
  # req.wait()





  data = None
  dados = None


data = comm.scatter(data, root=0)
data = primesNumbers(data["star"], data["end"])

# print(data["star"])
dados = comm.gather(data, root=0)
if dados:
  print(f'Rank: {rank} Total: ' , sum(dados))