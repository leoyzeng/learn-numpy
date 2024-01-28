import numpy as np


def main():

    # array
    array0 = np.array([1, 2, 3])
    print(array0)
    array1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(array1)
    array2 = np.array([[0,1,2,3,4,5,6,7], [8,9,10,11,12,13,14,15]])
    print()

    # dimension of array
    print(array1.ndim) # number of dimensions
    print(array1.shape) # size of array
    print()

    # get type
    print(array1.dtype) # data type
    print(array1.itemsize) # size of each element
    print(array1.nbytes) # total number of bytes of array
    print()

    # access array index
    print(array1[1, 2])
    # note: when accessing multi dimensional, always go outside in [outermost, middle, innermost]
    print(array1[1,-1])
    print(array1[2, :]) # get all of a row
    print(array1[:, 0]) # get all of a column
    print(array2[1,1: 6: 2]) # [start index: end index: step size]
    array0[1] = 10 # change element
    print(array0)
    array1[:,0] = 10 # change column
    print(array1)
    array2[1,1: 6: 2] = [20, 30, 40] # change 3 selected elements (start at [1,1], end at [1,6], increment by 2
    print(array2)
    print()

    # initialize arrays
    print(np.zeros((3,4,5))) # initialize array to 0s
    # note: pass in tuple, not individual numbers
    print(np.full((2,2), 10, dtype='float32')) # initialize array to value
    print(np.full_like(array0, 20)) # initialize array to same shape as array0
    print(np.random.rand(2,3)) # initialize array with random values between 0 and 1
    print(np.random.randint(5,10, size=(2,2))) # random ints from 5 to 10
    print(np.identity(4)) # identity matrix
    print(np.repeat([array0], 3, axis=0)) # repeat array 0 3 times
    array3 = np.zeros((5,5))
    array4 = np.ones((3,3))
    array3[1:4, 1:4] = array4 # replace section of array with something else
    print(array3)
    print()

    # copy
    array5 = array3 # copy reference/pointer
    array6 = array3.copy # make new array

    # math
    array7 = np.array([1,2,3,4])
    print(array7 + 2) # element arithmetic
    print(array7 * 2)
    array8 = np.array([2,3,4,5])
    print(array7 + array8) # add elements of 2 arrays
    print(np.sin(array7)) # sin

    # linear algebra
    array9 = np.ones((2,3))
    array10 = np.full((3,2),2)
    print(np.matmul(array9, array10)) # matrix multiplication
    array11 = np.full((3,3), 2)
    print(np.linalg.det(array11)) # determinant

    # stats
    print(np.min(array7)) # min value
    print(np.sum(array7)) # sum of values

    # reorganizing arrays
    print(array7.reshape((2,2))) # resize array dimensions
    print(np.vstack([array7, array8])) # stack 2 arrays vertically

    # other
    print(np.genfromtxt('data.txt', delimiter=',')) # get data from file
    print(array7[array7 > 2]) # only get indices greater than 2
    print(array7[[0,3]]) # index using a list
    array12 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
    print(np.any(array12 > 5))  # if any values in array is greater than 5
    print(np.any(array12 > 5, axis=1)) # if any row in array has value greater than 5
    print((array12 > 3) & (array12 < 10)) # if values are within range

    array13 = np.zeros((5,5))
    for i in range(0,5):
        for j in range(0,5):
            array13[i,j] = i*5+j

    print(array13)
    print(array13[2:4,0:2]) # indexing a box
    print(array13[[0,1,2,3],[1,2,3,4]]) # indexing a diagonal
    print(array13[[0,3,4], 3: ]) # indexing different rows

if __name__ == '__main__':
    main()

