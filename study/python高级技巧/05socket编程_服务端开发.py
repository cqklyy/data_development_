"""
演示Socket服务端开发
"""
import socket

# 创建Socket对象
socket_server = socket.socket()
# 绑定ip地址和端口
socket_server.bind(("localhost", 8888))
# 监听端口
socket_server.listen(1)  # listen方法内接收一个整数传参数，表示接收的链接数量
# 等待客户端连接
# result=socket_server.accept()       # accept返回的是二元元组（链接对象，客户端信息）
# conn=result[0]                      # 客户端和服务器的链接对象
# address=result[1]                   # 客户端的地址信息
conn, address = socket_server.accept()
# accept是阻塞的方法，等待客户端的链接，如果没有链接，就卡在这一行不向下执行
# 接受客户端信息
print(f'接收到了客户端的链接，客户端的信息是:{address}')

while True:

    # 接受客户端信息，要使用客户端和服务端的本次链接对象，而非socket_server对象
    data:str =conn.recv(1024).decode('UTF-8')
    # recv接受的参数是缓冲区大小，一般给1014即可
    # recv方法的返回值是一个字节数组也就是bytes对象，不是字符串，可以通过decode方法通过UTF-8编码将字节数组转换为字符串对象
    print(f"客户端发来的信息是：{data}")
    # 发送回复信息
    msg=input(f"请输入你和客户端发送的信息：")
    if msg=='exit':
        break
    conn.send(msg.encode('UTF-8'))

# 关闭链接
conn.close()
socket_server.close()


