import pandas as pd
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
df = pd.read_excel("Courses\\1sep\\sihx.xlsx")
# print(df.iloc[131])

# print(df.loc[df["Name3"] == "Eshit Saini"])
print(df.loc[df["Team Name"] == "Chilly Flicks" ])
# print(df["Problem Statement ID"] == 1614)
# print(df.iloc[233])
# l = []

# for i in range(0, 401):
#     print(df.iloc[i][["Name1"]+["Name2"]])
