# -*- coding: utf-8 -*-
__author__ = 'zhouxu'
'''
Statistics on the number of English words in a text file
'''
import sys


def countwords(filename):
    fin = open(filename)
    text = fin.read()
    text = text.replace("\n", " ")
    list = text.split(" ")
    return len(list)
