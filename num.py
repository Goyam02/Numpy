import numpy as np


a = np.array([1,2,3],dtype='int32') #1-D array
print(a) ## [1 2 3]



b = np.array([[9,8,10],[6,7,8]])  #2-D array
print(b) ## [[ 9  8 10]
         ##    [ 6  7  8]]

#Get dimension
print(a.ndim) ## 1
print(b.ndim) ## 2

#Get shape

print(a.shape) ## (3,)
print(b.shape) ## (2,3)


# Get the type 
print(a.dtype) ## int32
print(b.dtype) ## int64

#get item size
print(a.itemsize) ## 4 
print(b.itemsize) ## 8

#get size
print(a.size) ## 3
print(b.size) ## 6


#accessing/ changin gspecific elements,rows,columns etc,


c= np.array([[1,2,3,4,5,6,7],[2,3,4,5,6,7,8]])
print(c) ##  [[1 2 3 4 5 6 7]
         ##   [2 3 4 5 6 7 8]]

#get a specific element [r,c]

print(c[1,5]) ## 7

#get a specific row 
print(c[0,:]) ## [1 2 3 4 5 6 7]

# get  a specif column

print(c[:,3])  ##[4 5]

## getting a little more fancy [startIndex:endIndex:stepSize]

print(c[1,1:6:2]) ## [3 5 7]

## chaning element
c[1,5] = 20
print(c)


