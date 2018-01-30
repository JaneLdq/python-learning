#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
# 9, 9, 9 这三个函数延迟执行，此时调用i的值已经变成了3

def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立即执行，i当前值被传入
    return fs

f1, f2, f3 = count2()
print(f1(), f2(), f3())
# 1, 4, 9 这三个函数延迟执行，此时调用i的值已经变成了3
