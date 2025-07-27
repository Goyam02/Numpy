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

## 3-d example
d = np.array([[[1,2,3,4,5],[2,1,3,4,5]],[[1,2,3,4,5],[1,2,3,4,5]]])
print(d)
print(d.ndim)
print(d[1,0,2])
print(d[:,1,:])

## initialising differnet types of array

# all 0's matrix

print(np.zeros(5)) #[0. 0. 0. 0. 0.]

print(np.zeros((3,2,3)))  #[[[0. 0. 0.]
#                              [0. 0. 0.]]

#                           [[0. 0. 0.]
                            #   [0. 0. 0.]]

#                             [[0. 0. 0.]
#                                  [0. 0. 0.]]]

## all 1's matrix

print(np.ones((4,2,2),dtype='int32') ) ## can also specify the dtype

# any other number

print(np.full((2,2),99))   # have to pass 2 parameter shaope and the number  #[[99 99]
#  `                        [99 99]]


#any other numbe rfull_like
print(np.full_like(a,4)) # [4 4 4] 

#random numbers
print(np.random.rand(4,2))


#random integer values
print(np.random.randint(7,size=(3,3)))

#identity matrix

print(np.identity(5))

# # [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

## repeat an array
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)


##problem1
output = np.ones([5,5])
# print(output)

z= np.zeros([3,3])
z[1,1]=9
# print(z)

output[1:-1,1:-1]=z
print(output)

## be careful when copying arrays

a= np.array([1,2,3])
b=a.copy()
b[0]=100
print(b) #[100   2   3]
print(a) # [1 2 3]

### mathematics

a= np.array([1,2,3,4])
print(a)

print(a+2) 

b=np.array([2,3,4,5])


print(a+b)

## take the sin,cos

print(np.sin(a))
print(np.cos(a))

## linear algebra

a= np.full((2,3),2)
print(a)
b= np.full((3,2),2)
print(b)
#mat  multiplication
print(np.matmul(a,b))

# mat determinant
print(np.linalg.det(np.matmul(a,b)))


## statistics

stats = np.array([[2,5,6,7,8],[4,7,3,4,5]])
print(stats)
#find min
print(np.min(stats,axis=1))
#find max
print(np.max(stats))

print(np.max(stats,axis=0))

## reorganising arrays
before = np.array([[2,5,6,7,8],[4,7,3,4,5]])
print(before)

print(before)

after = before.reshape(5,2)
print(after)

##vertically staking vectors

v1= np.array([1,2,34,4,4])
v2 = np.array([3,6,7,7,7])

print(np.vstack([v1,v2,v1,v2,v2]))


## horizontal stack

print(np.hstack([v1,v2]))


## load from files
filedata = np.genfromtxt('sample_data.csv',delimiter=',',dtype='int32')
print(filedata)


## boolean masking and advaced indexing

print(filedata>50)
print(filedata[filedata>2])

print(np.any(filedata>5,axis=0))
print(np.all(filedata>5,axis=0))
