from data_define import Record
from file_define import FileReader, TxtFileReader, JsonFileReader
from pymysql import Connection
import pymysql

txt_file_reader = TxtFileReader("/data_input/数据分析案例/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("/data_input/数据分析案例/2011年2月销售数据JSON.txt")

jan_data: list[Record] = txt_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月份的数据合并成1个list来存储
all_data = jan_data + feb_data
# print(all_data)

conn = Connection(
    host="192.168.31.129",
    port=3306,
    user="root",
    password="20031201kK?",
    autocommit=True
)

cursor = conn.cursor()
conn.select_db("pymysql")
# for record in all_data:
#     sql=f"insert into py_mysql_database(order_data,order_id,money,province) values" \
#         f"('{record.date}','{record.order_id}',{record.money},'{record.province}')"
#     cursor.execute(sql)

sql_select = f"select * from py_mysql_database"
cursor.execute(sql_select)
print(cursor.fetchall())  # 打印从数据库查询到的信息

conn.close()
