import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

arr = np.random.rand(10,10)
sns.heatmap(arr, annot=True, cmap="coolwarm")
plt.title("Heatmap Example")
plt.show()