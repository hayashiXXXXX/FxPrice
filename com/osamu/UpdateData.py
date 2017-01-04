'''
Created on 2017/01/03

@author: o-komuro
'''

import re

from lib import Rakuten
from const import Const
from lib import Db


def updateData(brokerName, list):
    sql = "insert into price values"
    const = Const.Const()
    
    for k in list.keys():
        pattern = r"[0-9\.]+"
        matchlist = re.findall(pattern, list[k])
        b = matchlist[0]
        a = matchlist[1]
        s = round((float(a) - float(b)) * 100000) / 100000
        sql = sql + "('" + brokerName + "','" + k + "'," + str(b) + "," + str(a) + "," + str(s) + ", current_timestamp),"
    
    sql = sql[0:-1] + ";"
    
    print sql
    
    db = Db.Db()
    
    db.execute(const.POSTGRE_HOST, const.POSTGRE_PORT, const.POSTGRE_DB, const.POSTGRE_USER, const.POSTGRE_PW, "delete from price where broker='" + brokerName + "';")
    db.execute(const.POSTGRE_HOST, const.POSTGRE_PORT, const.POSTGRE_DB, const.POSTGRE_USER, const.POSTGRE_PW, sql)
    r = db.select(const.POSTGRE_HOST, const.POSTGRE_PORT, const.POSTGRE_DB, const.POSTGRE_USER, const.POSTGRE_PW, 'select * from price;')
    print r


const = Const.Const()
raku = Rakuten.Price()

raku_data = raku.getPrice(const.URL_RAKUTEN)

updateData("rakuten", raku_data)