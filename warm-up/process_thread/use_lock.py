#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import time, threading

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        # 用try/finally来确保锁一定会被释放
        try:
            change_it(n)
        finally:
            lock.release()
        # change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
