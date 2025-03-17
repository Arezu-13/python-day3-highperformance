from mpi4py import MPI

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()  # Get process rank
size = comm.Get_size()  # Get total number of processes

# Each process contributes its rank to the sum
local_value = rank      # Each process stores its rank in local_value

# Reduce all values to process with rank 0
# Aggregates all local_values (sums them) and sends the result to rank 0
total_sum = comm.reduce(local_value, op=MPI.SUM, root=0)    

# Print the result from process 0
# MPI ranks start from 0 and go up to size - 1, not size
if rank == 0:
    print(f"Total sum of ranks (0 to {size-1}): {total_sum}")
