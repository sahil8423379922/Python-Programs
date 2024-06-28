import numpy as np

# ar = np.array([1,2,3,4,5,6,7,8,9,10])
# print(ar.dtype)

# ar=np.array(["Sahil","Yash"])
# print(ar.dtype)

# i - integer
# b- boolean
# f- float
# c- complex float
# S-String

# ar = np.array([1,2,3,4,5,6,7,8,9,10],dtype='S')
# num= ar.astype('i')

# print(ar.dtype)
# print(num.dtype)

# ar = np.array([1,2,3,4,5,6,7,8,9])
# # x = ar.copy()
# # x[0]=10

# # y= ar.view()
# # y[0]=24

# # print(ar)
# # print(x)
# # print(y)

# print(ar.shape)

# nm =ar.reshape(3,3)
# print(nm)

ar = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])

# x =ar.reshape(2,3,2)

# print(x)
x = ar.reshape(-1)

print(x)


