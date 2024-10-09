import pandas as pd

df1 = pd.DataFrame({'key': ['a', 'b', 'c'], 'value1': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['b', 'c', 'd'], 'value2': [4, 5, 6]})

# Merge DataFrames based on the 'key' column
merged_df = pd.merge(df1, df2, on='key')
print(merged_df)

# Concatenate DataFrames vertically
concatenated_df = pd.concat([df1, df2])
print(concatenated_df)