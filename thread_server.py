"""
基于多线程的网络并发模型
重点代码 ！！

思路： 网络构建    线程搭建    /   具体处理请求
"""
from socket import *
from threading import Thread


# 处理客户端具体请求
class Handle:
    # 具体处理请求函数 （逻辑处理，数据处理）
    def request(self, data):
        print(data)


# 创建线程得到请求
class ThreadServer(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        self.handle = Handle()
        super().__init__(daemon=True)

    # 接收客户端的请求
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data:
                break
            self.handle.request(data)
        self.connfd.close()


# 网络搭建
class ConcurrentServer:
    """
    提供网络功能
    """
    def __init__(self, *, host="", port=0):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.sock = self.__create_socket()

    def __create_socket(self):
        tcp_socket = socket()
        tcp_socket.bind(self.address)
        return tcp_socket

    # 启动服务 --> 准备连接客户端
    def serve_forever(self):
        self.sock.listen(5)
        print("Listen the port %d" % self.port)

        while True:
            connfd, addr = self.sock.accept()
            print("Connect from", addr)
            # 创建线程
            t = ThreadServer(connfd)
            t.start()


if __name__ == '__main__':
    server = ConcurrentServer(host="0.0.0.0", port=8888)
    server.serve_forever()  # 启动服务
