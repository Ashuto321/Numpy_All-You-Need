import numpy as np
# creating a numpy array

myarr = np.array([3,6,32,7])
# you can also put datatypes in numpy like
# myarr = np.array([3,6,32,7], np.int8) #int8 for 8bit
# you can use int32,64 according to your needs

# if you want to know about the arrays row and column then 
# you can write
myarr = np.array([[3,6,32,7]]) #this is a 2D Array
# print(myarr.shape)
# print(myarr.dtype)
# lets change the element like
myarr[0,1]=45
# print(myarr)

#Array conversions from other python structures
listarray= np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(listarray)
# print(listarray.dtype)
# print(listarray.shape)
# print(listarray.size)


# for making zero array using numpy we have
zeros = np.zeros((2,5))
# print(zeros)

# for range.......
range = np.arange(15)
# print(range)

# for getting linspace
lspace = np.linspace(1,50,12)
# print(lspace)

# empty will help you 
emp = np.empty((4,6))

# print(emp)

# for creating identity
ide = np.identity(45)
# print(ide)
# print(ide.shape)

# one of the import function in numpy is reshape
arr = np.arange(99)
# print(arr)
# now you can reshape this arr 
# print(arr.reshape(3,33))
# so its like 3 * 33 = 99 so you have to 
# maintian the total shape.


# understanding axis in numpy
x = [[1,2,3], [4,5,6], [7,1,0]]
ar = np.array(x)
# print(ar)
# print(ar.sum(axis=0))#this will calculate 1+4+7
# print(ar.sum(axis=1)) #this will calculate 1+2+3

# now lets transpose the array 
# print(ar.T)

# now if well do flat that it will give me an iterator
# print(arr.flat)
# for item in arr.flat:
#        print(item)


# to get the dimention you can write 
# print(ar.ndim)
# print(arr.ndim)
# print(arr.size)
# print(ar.nbytes)

# usign the function argmax()

oned = np.array([1,2,3,9,456,6,7,8])

print(oned.argmax()) # gives you index of maxium value in the array
print(oned.argmin()) # gives you index of min value in the array

# argsort()--> this will help you gettig the indexs of elements in the sort form it should be 
print(oned.argsort())
# you can perform matrix operation on using numpy  
# like multiplication, division, and many more

# you can find the elements using where in numpy

print(np.where(ar>5))