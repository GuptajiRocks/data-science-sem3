import numpy as np
l = [10,20,30,5,50,72]
m = np.mean(l)
newl = []
std = 0

for i in l:
    std = std + (i-m)
    print(std)

print(std)
    
