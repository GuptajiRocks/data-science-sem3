import pandas as pd
import numpy as np

df1 = pd.read_csv("Practical\\14oct\\tit_tra.csv")

def q1():
    upperdf = df1["Name"].str.upper()
    print(upperdf)

def q2():
    less = df1["Name"]
    tx = less[0].split(",")
    tx2 = tx[1].split(" ")
    print(tx)
    print(tx2)
    print(tx2[1])
    

def q3():
    repl = df1["Name"].str.replace("Mr.","Mister")
    print(repl)

def q4():
    acount = df1["Name"].str.count('a')
    print(acount)

def q5():
    temps = df1["Name"]
    fl = []
    ll = []

    for i in temps:
        tem = i.split(",")
        fl.append(tem[1])
        ll.append(tem[0])
    
    tempdf = df1
    tempdf["First Name"] = fl
    tempdf["Last Name"] = ll

    print(tempdf)


q1()
q2()
q3()
q4()
q5()

