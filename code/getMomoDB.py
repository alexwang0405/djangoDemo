# -*- coding: utf-8 -*-
"""
momo

@author: Alex
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='password', database='django', charset='utf8')
cursor = conn.cursor()

driverpath='/home/alexwang/chromedriver'
driver=webdriver.Chrome(driverpath)

i=0
domain='https://www.momoshop.com.tw/'
# asus/acer/lenovo
brands = ['ASUS華碩','Acer宏碁','Lenovo聯想']
urls=['https://www.momoshop.com.tw/search/searchShop.jsp?keyword=%E7%AD%86%E9%9B%BB&searchType=1&cateLevel=0&cateCode=1200000000&curPage=1&_isFuzzy=0&brand=ASUS%20%E8%8F%AF%E7%A2%A9&brandNo=20160808155621011&showType=chessboardType',
      'https://www.momoshop.com.tw/search/searchShop.jsp?keyword=%E7%AD%86%E9%9B%BB&searchType=1&cateLevel=0&cateCode=1200000000&curPage=1&_isFuzzy=0&brand=Acer%20%E5%AE%8F%E7%A2%81&brandNo=20160808155608760&showType=chessboardType',
      'https://www.momoshop.com.tw/search/searchShop.jsp?keyword=%E7%AD%86%E9%9B%BB&searchType=1&cateLevel=0&cateCode=1200000000&curPage=1&_isFuzzy=0&brand=Lenovo&brandNo=20160808155811738&showType=chessboardType']


for url in urls:
    driver.get(url)
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    items = soup.find_all('a', class_='goodsUrl')
    
    for item in items:
        
        link = domain + item.get('href')
        title = item.find('p', class_='prdName').text
        money=item.find('b').text
        price = money.replace(',','')
        img = item.find('img').get('src')
        if item.find('p', class_='iconArea').text != '售完補貨中':
            sql="insert into shop(webname, title, photo, price, link, brand) values('momo','{}','{}',{},'{}','{}')".format(title, img, price, link, brands[i])
            cursor.execute(sql)
            conn.commit()
    
    i+=1

cursor.close()
conn.close()
driver.quit()
