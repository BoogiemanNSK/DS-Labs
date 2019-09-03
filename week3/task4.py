#!/usr/bin/python3
from threading import Thread
import time

arr = []


def func(a):
    time.sleep(1)
    arr.append(a)


if __name__ == "__main__":
    thread1 = Thread(target=func, args=(1,))
    thread1.start()
    thread2 = Thread(target=func, args=(6,))
    thread2.start()

    thread1.join()
    thread2.join()

    print("not empty list: ", arr)
