import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("Practical\\04nov\\Housing.csv")

def q1():
    plt.hist(df["price"], bins=30, color="blue", edgecolor="black")
    plt.xlabel("House Price")
    plt.show()

def q2():
    plt.scatter(df["price"], df["area"])
    plt.show()

def q3():
    tempdf = df[["price", "area", "bedrooms", "bathrooms", "stories", "parking"]]
    corr_mat = tempdf.corr()
    print(corr_mat)
    sns.heatmap(corr_mat, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

def q4():
    with_guest = df["guestroom"].value_counts()["yes"]
    without_guest = df["guestroom"].value_counts()["no"]
    mainroad_yes = df["mainroad"].value_counts()["yes"]
    mainroad_no = df["mainroad"].value_counts()["no"]
    print(with_guest, without_guest, mainroad_yes, mainroad_no)
    #tempdf = df[["mainroad", "guestroom"]]
    contingency_table = pd.crosstab(df['guestroom'], df['mainroad'])
    sns.heatmap(contingency_table, annot=True, cmap="coolwarm")
    plt.title("Mainroad and Guestroom correlation")
    plt.show()

def q5():
    print(df)
    counts = df["furnishingstatus"].value_counts()

    # plt.pie(counts, labels=counts.index)
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Distribution of furnished houses")
    plt.show()

q3()