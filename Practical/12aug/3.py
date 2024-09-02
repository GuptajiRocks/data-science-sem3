import pandas as pd

df = pd.read_csv('12aug\Salaries.csv')

def twenty_to_fifty():
    print(df.iloc[20:51])

def subset1():
    df2 = df[['discipline']]
    print(df2)

def uniqueval():
    uni = df['rank'].unique()
    print(uni)

# twenty_to_fifty()
# subset1()

uniqueval()