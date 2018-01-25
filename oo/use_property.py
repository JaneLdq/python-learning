#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name):
        self._name = name

    # 重写str方法
    def __str__(self):
        return 'Student object (name: %s)' % self._name.title()

    __repr__ = __str__

    @property
    def score(self):
        return self._score.title()

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # 不给setter就是一个只读属性了
    @property
    def age(self):
        return 2018 - self._birth

s = Student('jane')

print(s)
