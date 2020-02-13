import threading
import time


def test1():
    for i in range(5):
        time.sleep(1)
        print("---子线程1-----%d" % i)
        print("子线程1中查看线程情况", threading.enumerate())


def test2():
    for i in range(10):
        time.sleep(1)
        print("---子线程2-----%d" % i)
        print("子线程2中查看线程情况", threading.enumerate())


def main():
    # threading.enumerate():枚举当前的所有线程
    print("创建线程之前的线程情况", threading.enumerate())

    # 创建线程对象
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    time.sleep(1) # 休眠1秒
    print("创建线程之后的线程执行情况", threading.enumerate())

    t1.start()  # 开启线程
    t2.start()

    time.sleep(1)
    print("调用了thread.start()之后的线程情况", threading.enumerate())
    t2.join()  # 当t2线程执行完后，再执行后续的代码
    print("查看当前线程", threading.enumerate())


if __name__ == '__main__':
    main()