import numpy as np

arr = np.array([1,2,2,3,2,4])
print(arr)
print(type(arr))
print(np.__version__)
a1=np.array([1,2,3,4])  
print(a1.ndim,a1.size) 
a2=np.array([[1,2,3],[4,5,6]])  
print(a2.ndim,a2.size)  
a3=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]])  
print(a3.ndim,a3.size)  
print(a1.shape,a2.shape,a3.shape)