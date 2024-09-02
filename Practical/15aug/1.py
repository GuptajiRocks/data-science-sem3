from PIL import Image
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt


# im = Image.open('D:\\Bennett University\\Sem 3\\Data Analysis Using Python - CSET214\\Practical\\15aug\\one.jpg')
im = Image.open("Practical\\15aug\\one.jpg")
arr = np.array(im)

mask = np.full(arr.shape, 255)

mod = mask-arr
# mod = mod*-1

# mod = mod.astype(np.uint8)
plt.subplot(1,2,1)
plt.imshow(arr)
plt.subplot(1,2,2)
plt.imshow(mod)

plt.show()



