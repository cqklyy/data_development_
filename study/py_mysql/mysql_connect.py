"""
演示python pymysql库的基础操作
"""
from pymysql import Connection

# 构建MySQL数据库的连接
conn=Connection(
    host="192.168.31.129",  # 主机名（IP）
    port=3306,              # 端口
    user="root",            # 账户
    password="20031201kK?"  # 密码
)
# print(conn.get_server_info()) #打印mysql信息
# 执行非查询性质SQL
cursor=conn.cursor()        # 获取到游标对象
# 选择数据库
conn.select_db("")
# 执行sql
# cursor.execute("crate table test_pymysql(id int)")

# 执行查询性质SQL
cursor.execute("select * from student")

results=cursor.fetchall()
print(results)
for r in results:
    print(r)
# 关闭连接
conn.close()