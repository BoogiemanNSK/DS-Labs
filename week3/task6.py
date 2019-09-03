#!/usr/bin/python3
import hashlib
from threading import Thread
from timeit import timeit

# hashes of random str(int) from [0 ... 1_000_000]
TASKS = ['604678604882550e79d90fd9b29ecf34', '87456e18f180720ebaaf070f7d1e6e1c', '98222663d6fe9ea55efff46179d7c9b2',
         'c64a9829fa4638ff5de86330dd227e35', 'ca6bff62f4e46cbb192152ec843ebdbf', 'df7c2b3c3966426c14e4b3005c931eb1',
         '626103abae1be890f7d1c8148f9d690a', 'e31d05da308bf27ad15fedde779f2bc5', 'a2b12d7cf762d6cfb6ea086f9f492626',
         'a8573e231edaaedfb49ebfc14f4be808']


def solve(task):
    for i in range(10 ** 6):
        h = hashlib.md5(str(i).encode("utf-8")).hexdigest()
        if h == task:
            return


def multi():
    executors = []
    for task in TASKS:
        e = Thread(target=solve, args=(task,))
        e.start()
        executors.append(e)
    for e in executors:
        e.join()


def single():
    for task in TASKS:
        solve(task)


if __name__ == '__main__':
    # run function `number` times and return avg execution time
    res = timeit(multi, number=10)
    print("multi_thread", res)
    res = timeit(single, number=10)
    print("single_thread", res)
