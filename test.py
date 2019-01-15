# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 14:55
# @Author  : YuChou
# @Site    : 
# @File    : test.py
# @Software: PyCharm

class Test:
    def __init__(self,a):
        self.a = a
        self.b = None


if __name__ == "__main__":
    t = Test(0)
    T = t
    T.b = 2
    t.a =T.b
    print(t.a)
    print(T.a)