# -*- coding: utf-8 -*-
__author__ = 'zhouxu'
'''
save activation code to mysql database
'''
import mysql.connector
import random
config = {
    'user': 'zhouxu',
    'password': 'zhouxu',
    'host': '127.0.0.1',
    'database': 'activationcode',
}

'''
paramCode：要保存的激活码，这是一个列表
paramConfig：数据库的配置，这是一个字典
'''


def generate(lenth, quantity):
    ret = []
    for cnt in range(0, quantity):
        str = ""
        for i in range(0, lenth):
            str += chr(random.randint(33, 126))
        ret.append(str)
    return ret


def saveCode(paramCode, paramConfig):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    lenth = len(paramCode)
    sql = ("INSERT INTO code"" (id, code)"" VALUES(%s,%s)")
    for i in range(0, lenth):
        data = (i, paramCode[i])
        cursor.execute(sql, data)
    cnx.commit()
    cursor.close()
    cnx.close()

if __name__ == '__main__':
    ls = generate(10, 20)
    saveCode(ls, config)
