'''
Created on 2017/01/04

@author: o-komuro
'''

import psycopg2

class Db:
    
    def execute(self, host, port, dbname, user, passwd, sql):
        connection = psycopg2.connect("host=" + host + " port=" + port + " dbname=" + dbname + " user=" + user + " password=" + passwd)
        cur = connection.cursor()
        cur.execute(sql)
        connection.commit()
        cur.close()
        connection.close()
    
    def select(self, host, port, dbname, user, passwd, sql):
        connection = psycopg2.connect("host=" + host + " port=" + port + " dbname=" + dbname + " user=" + user + " password=" + passwd)
        cur = connection.cursor()
        cur.execute(sql)
        
        list = []
        for row in cur:
            list.append(row)
        cur.close()
        connection.close()
        return list
