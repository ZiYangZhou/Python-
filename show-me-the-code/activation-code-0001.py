# -*- coding: utf-8 -*- 
__author__ = 'zhouxu'
'''
generate activation code
'''
import random
import time

# 随机生成ASCCI码为33 - 126的字符作为激活码
# length为激活码的长度
# quantity为生成激活码的个数


def generate(lenth, quantity):
    ret = []
    for cnt in range(0, quantity):
        str = ""
        for i in range(0, lenth):
            str += chr(random.randint(33, 126))
        ret.append(str)
    return ret


if __name__ == '__main__':
    ret = generate(15, 4)
    print 'ret1', ret1
