import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(type(arr),arr.ndim,arr.shape,arr.size,arr.dtype)
a=np.array([[2,3],[5,6]],float)
b=np.array((2,5,6))
c=np.zeros((2,2))
d=np.full((2,2),6)
e=np.random.rand(2,2)
print(a,b,c,d,e)

p=np.array([[1,2,3],[4,5,6]])
r=np.array([[1,2,3],[4,5,6]])
print("Addition :",p+r)
print("Subraction :",p-r)
print("Multiplication:",p*r)
print("Division :",p/r)
print("modulus :",p**r)

m=np.array([[5,6,1],[2,3,4],[7,8,9]])
print(m.T)

data=[('Rejimol',2003,9.5),('Renuka',2003,9.5),('Mary Stella',1975,9.6),('Rejikumar',1969,9.5),('Ram',2019,9.8)]
dt=[('name','S10'),('yr',int),('cgpa',float)]
arr=np.array(data,dtype=dt)
print(data)
print(dt)
