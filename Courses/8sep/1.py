import math as m

def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)


def pr(x):
    res = ((m.floor(((fact(x))%(x+1))/x))*(x-1))+2
    print(res)

