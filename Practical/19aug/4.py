import numpy as np

# Create a 6x6 NumPy array
array = np.arange(36).reshape(6, 6)

# Calculate the middle indices
mid_row = (array.shape[0] - 1) // 2
mid_col = (array.shape[1] - 1) // 2

print(mid_row, mid_col)
# Extract the middlemost 4 elements
# middle_elements = array[mid_row-1:mid_row+2, mid_col-1:mid_col+2]

# print(middle_elements)