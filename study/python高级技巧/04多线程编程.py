"""
演示多线程编程的使用
"""

import time
import threading


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == "__main__":
    # 创建第一个线程
    sing_thread = threading.Thread(target=sing, args=("我要唱歌",))
    # 创建另一个线程
    dance_thread = threading.Thread(target=dance, kwargs={"msg": "我要跳舞"})

    # 让线程干活
    sing_thread.start()
    dance_thread.start()
