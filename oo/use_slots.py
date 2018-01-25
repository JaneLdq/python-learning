#!/usr/bin/env python3
#-*- coding: utf-8 -*-

class Student(object):
    # 使用__slot__限制允许绑定的属性名
    __slots__ = ('name', 'age')

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
# 子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class Graduate(Student):
    pass

s = Student()
s.name = 'Jane'
s.age = 22


try:
    s.gpa = 4.3
except AttributeError as e:
    print('AttributeError:', e)

g = Graduate()
g.gpa = 4.8
print('g.gpa = ', g.gpa)
