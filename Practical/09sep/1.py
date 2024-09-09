import pandas as pd

kdf = pd.read_csv("Practical\\09sep\\karate.csv", names=["Node_A", "Node_B"])
kwdf = pd.read_csv("Practical\\09sep\\kww.csv", names=["Node_A", "Node_B", "Weight"])

def p1():
    p1q1 =pd.merge(kwdf, kdf)
    print(p1q1)

def p2():
    a0q1df = pd.concat([kdf, kwdf], axis=0)
    a1q1df = pd.concat([kdf, kwdf], axis=1)
    print(a0q1df)
    print(a1q1df)


def p3():
    s1 = {"StudentID":[1,2,3], "Marks":[20,30,40], "Subject":["English","Hindi","Maths"]}
    s2 = {"StudentID":[2,3,8], "Marks":[40,100,240], "Subject":["English", "Hindi", "Maths"]}
    df1 = pd.DataFrame(s1)
    df2 = pd.DataFrame(s2)
    ans1 = pd.merge(df1,df2, on="StudentID")
    ans2 = pd.concat([df1, df2])
    print(ans1)
    print(ans2)

