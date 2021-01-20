from socket import *

# 服务端地址
ADDR = ("127.0.0.1",8888)

tcp_socket = socket()
tcp_socket.connect(ADDR)

# 循环发送接收消息
while True:
    msg = input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())

tcp_socket.close()