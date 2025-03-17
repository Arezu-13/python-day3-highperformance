import numpy as np

# 2a : 
a = np.zeros(10)
a[[4]] = 1
#print(a)

# 2b :
b = np.arange(10, 50)
#print(b)

# 2c :
c = np.arange(10)
d = c[::-1]
#print(c)
#print(d)

# 2d :
e = np.arange(0,9).reshape(3, 3)
#print(e)

# 2e :
f = np.array([1,2,0,0,4,0])
g = np.nonzero(f)
#print(f)
#print(g)

# 2f :
h = np.random.random(30)
i = np.mean(g)
#print(h)
#print(i)

# 2g :
j = np.zeros(20).reshape(4, 5)
j[:, 0] = 1
j[:, 4] = 1
j[0, :] = 1
j[3, :] = 1
#print(j)

# 2h :
k = np.zeros(64).reshape(8, 8)
k[0][:2] = 1
k[1][:2] = 1
k[4][:2] = 1
k[5][:2] = 1
k[0][4:6] = 1
k[1][4:6] = 1
k[4][4:6] = 1
k[5][4:6] = 1

k[2][2:4] = 1
k[3][2:4] = 1
k[2][6:8] = 1
k[3][6:8] = 1
k[6][2:4] = 1
k[7][2:4] = 1
k[6][6:8] = 1
k[7][6:8] = 1
#print(k)

# 2i :
l = np.array([[0, 1], [1, 0]])
m = np.tile(l, (4, 4))
#print(m)

# 2j :
o = np.arange(11)
o[(o > 3) & (o < 8)] *= -1
#print(o)

# 2k :
p = np.random.random(10)
q = np.sort(p) 
#print(p)
#print(q)

# 2l :
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.array_equal(A, B)  # not equal, i.e false since A and B generate numbers randomly
#print(equal)

# 2m :
r = np.arange(10, dtype=np.int32)
#print(r.dtype)
s = np.arange(10, dtype=np.int32)**2
#print(s, s.dtype)

# 2n :
t = np.arange(9).reshape(3,3)
u = t + 1
v = np.dot(t,u)
w = np.diagonal(v)
#print(v)
#print(w)