# -*- coding: utf-8 -*-
"""
pchome
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='password', database='django', charset='utf8')
cursor = conn.cursor()

driverpath = '/home/alexwang/chromedriver'
driver = webdriver.Chrome(driverpath)

i=0
domain='https://mall.pchome.com.tw/'
# acer/asus/lenovo
brands = ['Acer宏碁','ASUS華碩','Lenovo聯想']
urls=['https://mall.pchome.com.tw/store/QAAH0G','https://mall.pchome.com.tw/store/QAAH0Q','https://mall.pchome.com.tw/store/QAAH19']


for url in urls:
    driver.get(url)
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    content = soup.find('dl', id='storeprod')
    items = content.find_all('dd')
    
    for item in items:
        
        link = domain + item.find('a').get('href')
        title = item.find('a', id='nick').text
        img = item.find('img').get('src')
        price=item.find('span', class_='value').text
        
        sql="insert into shop(webname, title, photo, price, link, brand) values('pchome','{}','{}',{},'{}','{}')".format(title, img, price, link, brands[i])
        cursor.execute(sql)
        conn.commit()
    
    i+=1
    
cursor.close()
conn.close()
driver.quit()
