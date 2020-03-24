# -*- coding: utf-8 -*-
"""
暢銷書籍
@author: Alex
"""

import requests
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='password', database='django', charset='utf8')
cursor = conn.cursor()

books=['python','java','android','C語言','html']
header={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

for book in books:
    url='https://search.books.com.tw/search/query/cat/all/key/{}/v/1/ms2/ms2_1'.format(book)
    text = requests.get(url, headers=header).text
    soup = BeautifulSoup(text, 'html.parser')
    data = soup.find_all('li', class_='item')
    for row in data:
        link = row.find('a').get('href')
        image = row.find('img').get('data-original')
        title = row.find('h3').text
        price = row.find('strong').find('b').text
        
        sql="insert into book(kind, link, title, image, price) values('{}','{}','{}','{}',{})".format(book, link, title, image, price)
        cursor.execute(sql)
        conn.commit()
    
cursor.close()
conn.close()

