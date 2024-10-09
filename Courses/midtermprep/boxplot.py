# import matplotlib.pyplot as plt


# data = [35, 42, 47, 50, 53, 57, 62, 65, 70, 75]

# plt.boxplot(data, vert=False)
# plt.show()

# import numpy as np
# x = np.array([35, 42, 47, 50, 53, 57, 62, 65, 70, 75])
# print(np.std(x))

#data = [35, 42, 47, 50, 53, 57, 62, 65, 70, 75]
data = [150, 160, 165, 170, 175]
mn = sum(data)/len(data)

summation = 0
for i in data:
    summation = summation + ((i-mn)**2)

std = (summation/len(data))**0.5

zarr = []

for i in data:
    zarr.append((i-mn)/std)

print(zarr)


