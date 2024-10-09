import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice'],
        'Age': [25, 30, 22, 28, 25],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'New York']}
df = pd.DataFrame(data)

# Group by 'City' and calculate the mean age for each city
grouped_df = df.groupby('City')['Age'].count()
print(grouped_df)

