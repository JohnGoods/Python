# 引入threading线程模块
import threading
import time


def download_music():
    """模拟下载歌曲，需要5秒钟下载完成"""
    for i in range(5):
        time.sleep(1)  # 休眠1秒
        print("---正在下载歌曲%d---" % i)


def play_music():
    """模拟播放歌曲，需要5秒钟下载完成"""
    for i in range(5):
        time.sleep(1)  # 休眠1秒
        print("---正在播放歌曲%d---" % i)

def main():
    t1 = threading.Thread(target=download_music)
    t2 = threading.Thread(target=play_music)

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()