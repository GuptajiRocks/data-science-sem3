import pandas as pd

df = pd.read_csv('12aug\Housing.csv')
# pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns', None)


def printfive():
    print(df.head())

def printshape():
    print(df.shape)

def stats():
     print(df.describe())

def newdataset():
    df2 = df[['price','bedrooms','bathrooms','stories','parking','furnishingstatus']]
    print(df2)

def uniquevalue():
    print(df['furnishingstatus'].value_counts())
# stats()
#printshape()
# newdataset()
# print(df)

uniquevalue()
