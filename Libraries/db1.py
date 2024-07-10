import pymysql

mydb = pymysql.connect(
    host="<host>",
    user="root",
    password="<password>",
)

mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
databases = mycursor.fetchall()
print("available databses")
for db in databases:
    print(db[0])

selected_db = input("\nEnter the name of the database you want to use: ")
if (selected_db,) in databases:
    # Connect to the selected database
    mycursor.execute(f"USE {selected_db}")

    mycursor.execute("SHOW TABLES")
    tables = mycursor.fetchall()
    for tb  in tables:
        print(tb[0])

mycursor.close()
mydb.close()