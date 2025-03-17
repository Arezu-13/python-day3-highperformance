import numpy as np

# a :
p = np.array([[1.0, 2.0, 10],
 [3.0, 4.0, 20],
 [5.0, 6.0, 30],
 [7.0, 8.0, 40]])

# Extracting last column
z = p[:,2]

# Reshaping z to 2D array
z = z.reshape(4,1)

# Normalizing
n = p / z
#print(n)

# b : 
arr = np.random.rand(3, 3)
#print(arr)
diagonal_arr = arr[np.arange(3), np.arange(3)]
#print(diagonal_arr)

# c :
A = np.random.rand(10, 3)

#  absolute difference from 0.75
diff = np.abs(A - 0.75)

# Find the index of the column with the closest element for each row using np.argmax
indices = np.argmax(-diff, axis=1) # negative diff to get the smallest absolute difference

# fancy indexing to extract the closest values from each row
closest_values = A[np.arange(10), indices]

#print(A)
#print(indices)
#print(closest_values)

# d : 
x = np.empty((10, 8, 6))

idx0 = np.zeros((3, 8)).astype(int)
idx1 = np.zeros((3, 1)).astype(int)
idx2 = np.zeros((1, 1)).astype(int)

B = x[idx0, idx1, idx2] # shape of x[idx0, idx1, idx2] is (3, 8, 1).
#print(B.shape)

# e : 
E = np.arange(12, dtype=np.int32).reshape((3, 4))

# output array has 2 windows for each of the 3 rows, 
# each with 2 elements along both axes (rows and columns).
# hence the shape (2, 3, 2, 2) i.e 4D array
striding = np.lib.stride_tricks.as_strided(
    E, shape=((2, 3, 2, 2)), strides=[E.strides[0], E.strides[1], E.strides[0], E.strides[1]])
print(striding)