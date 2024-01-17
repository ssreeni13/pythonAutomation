import mysql.connector

# insert, update, delete
insert_query = "insert into student values(104,'Kim')"
update_query = "update student set sname='Mary' where sid=104"
delete_query = "delete from student where sid=104"

try:
    con = sql.connector.connect(host="localhost", port=3307, user="root", passwd="root", database="mydb")
    curs = con.cursor()  # Create Cursor
    curs.execute("select * from orders")  # execute query through cursor

    for row in curs:
        print(row[0],row[1],row[2])

    con.close()
except:
    print("Connection Unsuccessful....")

print("Finished.......")