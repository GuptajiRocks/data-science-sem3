import pandas as pd
import re

def q1a():
    x = "Call us at 666-232-3403 or (666) 232 3403 and find your details"
    pattern = r'\$\d+(?:\.\d{2})?'
    matches = re.findall(pattern, x)
    for m in matches:
        print(m)

def q1b():
    data = " The unicorn is an element of a myth, it is magical and unique. An igloo, an island, and an umbrella are all interesting examples."
    pattern = r"\b[aeiou][a-z]*[bcdfghjklmnpqrstvwxyz]\b"
    matches = re.findall(pattern, data)
    for m in matches:
        print(m)

def q1c():
    data = "The items are priced at $3.45, $23.32, and $400. Additional fees of $5.99 apply."
    
    pattern = r"\$\d+\.{1}\d*"
    matches = re.findall(pattern, data)
    for m in matches:
        print(m)

def q1d():
    data = {'company_code': ['Abcd','EFGF', 'zefsalf', 'sdfslew', 'zekfsdf'],'date_of_sale': ['12/05/2002', '16/02/1999', '25/09/1998', '12/02/2022','15/09/1997'],'sale_amount': [12348.5, 233331.2, 22.5, 2566552.0, 23.0]}
    df = pd.DataFrame(data)
    df["cclen"] = df["company_code"].str.len()
    df["saleamtlen"] = df["sale_amount"].astype(str).str.len()
    print(df)
    return df

def q1e():
    df = q1d()
    l = list(df["date_of_sale"])
    print(l)
    jl = []
    pattern = r"\d{4}"
    for i in l:
        tl = re.findall(pattern, i)
        jl.extend(tl)

    df["year_of_sale"] = jl
    print(df)

# x = q1d()
q1e()
