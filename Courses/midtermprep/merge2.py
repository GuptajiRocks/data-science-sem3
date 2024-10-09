import pandas as pd

# Creating the customers DataFrame
customers = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 25, 35]
})

# Creating the transactions DataFrame
transactions = pd.DataFrame({
    'TransactionID': [101, 102, 103, 104],
    'CustomerID': [1, 2, 2, 3],
    'Amount': [100.50, 250.75, 75.00, 120.00]
})

# Merging the two DataFrames on CustomerID
merged_data = pd.merge(transactions, customers, on='CustomerID')

# Displaying the merged DataFrame
print(merged_data)
