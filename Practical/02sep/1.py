file = open("Practical\\02sep\\file1.txt", 'r')
file2 = open("Practical\\02sep\\water.png", "rb")
def q1():
    # When opening in write mode, the file is completely cleared, because existing data is overwritten
    for each in file:
        print(each)

def q2():
    img_txt = file2.read()
    print(img_txt)
    print(f"{len(img_txt)} is the size of the image")

def q3():
    print(file.read(4))

def q4():
    l = [i for i in file]
    print(l)

q4()
file.close()
file2.close()
