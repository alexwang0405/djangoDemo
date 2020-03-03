# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='password', database='django', charset='utf8')
cursor = conn.cursor()

stocks = ['2357','2376','2454']
stockname=['華碩','技嘉','聯發科']
i=0

for stock in stocks:
    url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?date={}&stockNo={}'.format('20200201', stock)
    res = requests.get(url)
    datas = res.json()
    for data in datas['data']:
        y,m,d = data[0].split('/')
        date = str(y) + str(m) + str(d)
        openprice = data[3]
        endprice = data[6]
        
        sql="insert into stock(name, no, openprice, endprice, date) values('{}','{}',{},{},'{}')".format(stockname[i], stock, openprice, endprice, date)
        cursor.execute(sql)
        conn.commit()
    i+=1
cursor.close()
conn.close()
