import pandas as pd

df = pd.read_csv("Practical\\09sep\\dmd.csv")
print(df)
print(df.isnull())

print(df["Serum_Insulin"].fillna(df["Serum_Insulin"].mean()))
print(df["Serum_Insulin"].fillna(0))

df_cleaned = df.dropna(subset=None)
print(df_cleaned)