#!/usr/bin/python3
import threading
from threading import Thread
import time


def func(a, b, name):
    while True:
        a = a + b
        print("{}: {}".format(name, a))
        time.sleep(1)


if __name__ == "__main__":
    thread1 = Thread(target=func, args=(5, 6, "thread1"), daemon=True)
    thread2 = Thread(target=func, args=(1, 2, "thread2"), daemon=True)

    thread1.start()
    thread2.start()

    while True:
        print("Total number of threads: {}".format(threading.activeCount()))
        print("List of threads: {}".format(threading.enumerate()))
        time.sleep(5)
