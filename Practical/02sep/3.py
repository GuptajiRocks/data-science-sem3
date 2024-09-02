import os
cs = os.getcwd()

file1 = open("Practical\\02sep\\f1.txt", "r")
file2 = open("Practical\\02sep\\f2.txt", "a")

data = file1.read()
file2.write(data)

print(data.count("this"))

print(f"Current working directory is: {cs}")

