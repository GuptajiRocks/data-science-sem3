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

def get_data_from_db():
    mydb = mc.connect(
    host="localhost",
    user="root",
    password="root",
    database="paymentsinfraone"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM transactions")
    myresult = mycursor.fetchall()
    mydb.close()
    return myresult

def get_transac_by_id(sid):
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="root",
        database="paymentsinfraone"
    )

    mycursor = mydb.cursor()

    try:
        sql = "SELECT * FROM transaction WHERE senderID = %s"
        mycursor.execute(sql, sid)
        mydb.commit()
        mydb.close()
    except:
        return 0

    return 1






