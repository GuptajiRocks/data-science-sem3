import mysql.connector as mp

connection = mp.connect(host='localhost', database="pysqlone",user="root", password="root")
pmt = "What comes under magma"
otpt = "Nothing you retard"
cursor = connection.cursor()
insert_query = f"INSERT INTO prompthistory VALUES(\"{pmt}\", \"{otpt}\");"

cursor.execute("USE pysqlone;")
cursor.execute(str(insert_query))
connection.commit()