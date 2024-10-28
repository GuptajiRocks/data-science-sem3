import numpy as np
l = [10,20,30,5,50]
m = np.mean(l)
newl = []

std_dev = 0

for i in l:
    std_dev = std_dev + (i-m)

tv = std_dev/len(l)
res = tv**0.5

for i in l:
    newl.append((i-m)/res)

print(newl)
