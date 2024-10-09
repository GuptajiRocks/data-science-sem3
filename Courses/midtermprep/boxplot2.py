import matplotlib.pyplot as plt

data = [10,90,34,21,43,28,98,46]
data.sort()
print(data)
plt.boxplot(data, vert=False)
plt.show()
