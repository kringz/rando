import pymysql
import random

#
# mysql creds

mydb = pymysql.connect(
    host="127.0.0.1",
    user="user",
    passwd="password",
    database="database"
)

min_id = 1 # set bottom of range
max_id = 500000 # set top of range

# select the range of rows in your table

mycursor_all_1 = mydb.cursor()
sql_all_1 = "SELECT * FROM `table` WHERE id >'" + str(min_id) + "' AND id <'" + str(max_id) + "'"
mycursor_all_1.execute(sql_all_1)
myresult_all_1 = mycursor_all_1.fetchall()

for x in myresult_all_1:

    # generate a random number based on your range

    numb=(random.randint(min_id,max_id))
    numb=str(numb)

    # select a row with id=numb

    mycursor_all_2 = mydb.cursor()
    sql_all_2 = "SELECT * FROM `table` WHERE id =" + numb
    mycursor_all_2.execute(sql_all_2)
    myresult_all_2 = mycursor_all_2.fetchall()

    # update a column in the row

    for y in myresult_all_2:
        domain = y[0]
        id_1 = y[3]
        id_1 = str(id_1)
        print(domain)
        print(id_1)
        sql_update = "UPDATE table SET column_name = '1' WHERE id =" + id_1
        mycursor_all_2.execute(sql_update)
        mydb.commit()

mycursor_all.close()
mydb.close()
