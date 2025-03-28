from pymysql import Connection

conn=Connection(
    host="192.168.31.129",
    port=3306,
    user="root",
    password="20031201kK?"
)

cursor=conn.cursor()
conn.select_db("")
cursor.execute("insert into table values() ")
conn.commit()


conn.close()