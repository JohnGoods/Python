import socket


def main():
    # 1. 创建udp socket套接字对象
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 通过udp socket发送消息
    # 2.1 准备目标主机的ip地址和端口号
    dest_addr = ("192.168.1.137", 8080)
    # 是一个元组类型，第一个元素是字符串，是目标主机的ip的地址
    # 第二个元素是整数 ，是目标主机的进程的端口号

    # 2.2  取得要发送的数据
    send_data = input("请输入要发送的数据:")

    # 2.3 发送数据到目标主机
    udp_socket.sendto(send_data.encode("utf-8"), dest_addr)  # 第一个参数是要发送的数据，第二个参数是目标主机地址

    # 3. 等待从目标主机回传的消息 ，它是阻塞状态
    recv_data = udp_socket.recvfrom(1024)  # buffersize : 缓存的大小，一次最多接收多少字节的数据

    # 4. 显示接收到的消息
    # 回传的消息： (b'good', ('192.168.236.129', 8080))
    # 元组类型，第一个元素是回传的消息 ，第二个是目标主机的ip和端口
    recv_info=recv_data[0].decode("utf-8") # 解码，把字节串转换为字符串
    recv_addr=str(recv_data[1])
    print("接收到的消息:%s ,消息来自<<<%s" %(recv_info,recv_addr))

    # 5. 关闭socket套接字
    udp_socket.close()


if __name__ == '__main__':
    main()