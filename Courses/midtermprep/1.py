import pandas as pd

data = {"A":[3,2,1], "B":[4,5,6], "C":[7,8,9]}
df = pd.DataFrame(data)
#print(df.iloc[[1,2],[1,2]])

# dictionary database when given, always convert to row column form, asaan rahega

#print(df.sort_values("A"))
def groups():
    newdf = df.groupby("A")
    print(newdf)

def strings():
    x = "Arihant"
    print(x[-1])

strings()