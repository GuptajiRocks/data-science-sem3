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
    txt = ",,,,,rrttgg.....banana....rrr"
    #x = "arihant"
    x = txt.strip(",.grt")
    print(x)

def strings2():
    txt = "arihant"
    new_txt = txt.strip('at')
    text = "abcdeabc"
    stripped_text = text.strip('a')
    print(stripped_text)
    print(new_txt)

def replace1():
    txt = "abcdeabc"
    new = txt.replace("a", "").replace("b", "")
    print(new)

def strings3():
    txt = "####Hello,World!###"
    res = txt.strip('#')
    print(res)
strings3()
#replace1()