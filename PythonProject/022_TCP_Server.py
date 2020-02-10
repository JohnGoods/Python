import socket

# 创建socket
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 本地信息
address = ('', 7788)

# 绑定
tcp_server_socket.bind(address)

# 使用socket创建的套接字默认的属性是主动的，使用listen将其变为被动的，这样就可以接收别人的连接请求
tcp_server_socket.listen(5) # backlog=5 表示积压的客户端连接请求最多5个， 超过5个，则拒绝连接

# 如果有新的客户端来连接服务器，那么就产生一个新的套接字专门为这个客户端服务
# new_socket用来为这个客户端服务
# tcp_server_socket就可以省下来专门等待其他新客户端的连接
new_socket, clientAddr = tcp_server_socket.accept()

# 接收对方发送过来的数据
recv_data = new_socket.recv(1024)  # 最多接收1024个字节
print('接收到的数据为:', recv_data.decode('gbk'))

# 发送一些数据到客户端
new_socket.send("thank you !".encode('gbk'))

# 关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
new_socket.close()