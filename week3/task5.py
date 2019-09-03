#!/usr/bin/python3
from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, thread_id, name, delay):
        super().__init__()
        self.threadID = thread_id
        self.name = name
        self.delay = delay

    def run(self):
        print("Starting ", self.name)
        print_time(self.name, 5, self.delay)
        print("Exiting ", self.name)


def print_time(thread_name, counter, delay):
    while counter:
        time.sleep(delay)
        print("%s: %s sec" % (thread_name, time.strftime("%S", time.gmtime())))
        counter -= 1


if __name__ == "__main__":
    # Create new threads
    thread1 = MyThread(1, "Thread-1", 1)
    thread2 = MyThread(2, "Thread-2", 2)

    # Start new Threads
    thread1.start()
    thread2.start()

    print("Exiting Main Thread")
