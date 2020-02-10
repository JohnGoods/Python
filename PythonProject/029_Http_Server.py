import socket


def handle_client(client_socket):
    """处理浏览器客户端的请求"""

    # 等待接收客户端发送的消息
    recv_data = client_socket.recv(4096)

    # 解码数据
    request_data = recv_data.decode("utf-8")

    # 显示接收到的请求报文数据
    print(request_data)

    # 按照http 响应报文格式去回复客户端
    """http 响应报文格式
     1. 响应行 ： HTTP/1.1 200 OK
     2. 响应头 Server: mimiweb1.0    Connection: Keep-alive
     3. 分隔符 \r\n
     4. 响应体  very good
    """
    response_line = "HTTP/1.1 200 OK\r\n"  # 响应行，必须有
    response_headers = "Server: mimiweb1.0\r\n"
    response_headers += "Connection: Keep-alive\r\n"
    split = "\r\n"  # 请求头与请求体的分隔符
    response_body = "very good?\r\n"

    # 拼接响应报文数据
    response_datas = response_line + response_headers + split + response_body

    # 向客户端发送响应报文数据
    client_socket.send(response_datas.encode("utf-8"))

    # 关闭套接字
    client_socket.close()


def main():
    """程序主控制入口"""

    # 创建监听套接字
    http_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 当套接字四次挥手，可立即复用地址端口
    http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 服务端绑定端口
    http_server_socket.bind(('', 7788))

    # 开启监听
    http_server_socket.listen(128)

    # 等待接受浏览器客户端的请求
    while True:
        client_socket, client_addr = http_server_socket.accept()
        print("有新的客户端请求,来自>>>", client_addr)

        # 在函数中为客户端提供服务
        handle_client(client_socket)


if __name__ == '__main__':
    main()