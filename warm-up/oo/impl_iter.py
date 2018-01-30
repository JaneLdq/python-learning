#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    # 实现__iter__()方法，可以使实例用于for...in循环
    # 返回一个迭代对象，在这里返回自身
    def __iter__(self):
        return self

    # 实现__next__()方法用于获取下一个元素
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        # 结束循环
        if self.a > 100:
            raise StopIteration()
        return self.a

f = Fib()

for x in f:
    print(x)
