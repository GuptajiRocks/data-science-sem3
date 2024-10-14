import pandas as pd
df = pd.read_csv("Practical\\14oct\\emp_pro.csv")
print(df)

def q1():
    regs = df["region"]
    l = []
    for i in regs:
        tem = i.split("_")
        l.append(tem[1])
    
    print(l)

def q2():
    unqdept = df["department"].unique()
    print(unqdept)

def q3():
    temp = df["recruitment_channel"]
    unqrec = temp.value_counts()
    print(unqrec)

def q4():
    df.columns = df.columns.str.replace('_', '')
    print(df)

q1()

