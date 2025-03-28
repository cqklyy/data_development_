"""
演示Socket客户端开发
"""
import socket

# 创建Socket对象
socket_client = socket.socket()
# 连接到服务器
socket_client.connect(("localhost", 8888))

while True:

    # 发送消息
    msg=input("请输入要发送的消息：")
    socket_client.send(msg.encode('UTF-8'))
    if msg=='我要走了':
        break
    # 接受返回信息
    recv_data=socket_client.recv(1024)        # 1024是缓冲区大小，同样recv方法是阻塞的

    print(f"服务端回复的信息是：{recv_data.decode('UTF-8')}")

# 关闭链接
socket_client.close()
