import mysql.connector as mc

mydb = mc.connect(
    host="localhost",
    user="root",
    password="root",
    database="paymentsinfraone"
)

mycursor = mydb.cursor()

def insertMoney(sid, rid, amt):
    sql = "INSERT INTO transactions (senderID, recID, amount) VALUES(%s, %s, %s)"
    val = (sid, rid, amt)
    try:
        mycursor.execute(sql, val)
    except:
        return 0

    mydb.commit()
    return 1


mydb.close()

