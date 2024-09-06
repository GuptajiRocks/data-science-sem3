import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

df = pd.read_excel("Lectures\\06sep\\csijc.xlsx", sheet_name="Research")

#print(df[["Name", "Email"]])
print(df["Name"])
print(df.iloc[[0,2,3,4,5,6,10,11,13,16]][["Name","Email"]])