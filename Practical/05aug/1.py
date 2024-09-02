import numpy as np
import random

def ques1():    
    n = np.eye(3)
    print(n)

def ques2():    
    n = np.arange(9).reshape(3,3)
    print(n)

def ques3():    
    n = np.arange(16).reshape(4,4)
    print(n)


def ques4(rows, cols, min_val, max_val):

  array = []
  for _ in range(rows):
    row = [random.randint(min_val, max_val) for _ in range(cols)]
    array.append(row)
  return array

def ques5():
   array = [random.randint(0,6) for _ in range(15)]
   print(array)

def ques6():
   array = [random.randint(0,50) for _ in range(50)]
   print(array)
   array.reverse()
   print(array)

def ques7():
   array = np.arange(12).reshape(3,4)
   print(array)
   array.reshape(2,2,3)
   print(array)

def ques8(x):
   temp=[]
   for i in range(len(x)):
      if x[i] == 0:
         temp.append(i)
   print(temp) 
         
def ques10():
   m = np.arange(27).reshape(3,3,3)
   print(m)
   maxval = m.max()
   minval = m.min()

   print(minval, maxval)




    