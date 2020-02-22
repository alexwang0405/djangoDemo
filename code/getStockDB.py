# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='123456789', database='django', charset='utf8')
cursor = conn.cursor()

stocks = ['2330']

for stock in stocks:
    url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?date={}&stockNo={}'.format('20191101', stock)
    res = requests.get(url)
    datas = res.json()
    for data in datas['data']:
        date = data[0]
        price = data[6]
        print(date, price)
        sql="insert into stock(name, datetime, price) values('{}','{}',{})".format(stock, date, price)
        cursor.execute(sql)
        conn.commit()
    
cursor.close()
conn.close()