import mysql.connector as mc


def insertMoney(sid, rid, amt):
    mydb = mc.connect(
    host="localhost",
    user="root",
    password="root",
    database="paymentsinfraone"
    )

    mycursor = mydb.cursor()
    
    sql = "INSERT INTO transactions (senderID, recID, amount) VALUES(%s, %s, %s)"
    val = (sid, rid, amt)
    try:
        mycursor.execute(sql, val)
    except:
        return 0

    mydb.commit()
    mydb.close()
    return 1


