from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
name = MPI.Get_processor_name()
size = comm.Get_size()
# print(name, size, rank)

if rank == 0:
    for r in range(size):
      data = {'Tarefa': r, 'dados': ((r+1)**r) * 99}
      req = comm.isend(data, dest=r, tag=11)
      req.wait()
# elif rank == 1:

else:
    req = comm.irecv(source=0, tag=11)
    data = req.wait()
    print(f'O Rank {rank} recebeu: {data} do rank 0')


