import mysql.connector as mp
import numpy as np

connection = mp.connect(host="mysql-demo1-arihantguptaheadboy-1787.a.aivencloud.com", port=16535, database="promptone", user="avnadmin", password="AVNS_7LB6ypURzGIqCL9_mcn")

mycursor = connection.cursor()

id = str(np.random.randint(1, 15001))
x = "My name is Arihant"
otpt = "Ok, Lets see"


insert_query = f"INSERT INTO pmthist VALUES({id}, \"{x}\", \"{otpt}\");"

mycursor.execute(insert_query)


