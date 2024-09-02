import numpy as np 

arr = np.array([[67,55,77,69],
               [83,79,92,88],
               [87,93,94,90],
               [84,81,76,77],
               [65,69,59,64]])

def sort_acc_rows(x):
    sortedx = np.sort(x,axis=1)
    print(sortedx)

def sort_acc_col(x):
    sortedy = np.sort(x,axis=0)
    print(sortedy)

def flat_array():
    arr1 = arr.flatten()
    print(arr1)

def create_zero_ones():
    m = np.zeros((5,4))
    m[0,:] = 1
    m[-1,:] = 1
    m[:,0] = 1
    m[:, -1] = 1
    print(m)

def max_val_axisone(x):
    arrmax = np.argmax(x, axis=1)
    print(arrmax)

def replace_minusone():
    arr[(arr>70) & (arr<80)] = -1
    print(arr)

def access_first_and_last(x):
    print(x[0])
    print(x[-1])

access_first_and_last(arr)

