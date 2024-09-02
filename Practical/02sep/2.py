def q1():
    l =[]
    # l2 = ["Arihant\n", "Arastu\n", "Vansh\n", "Vishnu\n", "Pallav\n"]
    for i in range(5):
        x = str(input("Enter name of friend: "))
        l.append(x+"\n")

    file = open("Practical\\02sep\\two.txt", "a")

    for i in l:
        file.write(i)

def q2():
    data = [1,2,3,4,5]
    with open('Practical\\02sep\\one.bin', 'wb') as file:
        file.write(bytes(data))
    
    with open("Practical\\02sep\\one.bin", "rb") as f:
        data = f.read()

    print(data)

q2()
