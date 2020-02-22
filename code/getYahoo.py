# -*- coding: utf-8 -*-
"""
從yahoo爬筆電資料

@author: Alex
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pymysql

connect=pymysql.connect(host='localhost', user='root', password='password', database='django', charset='utf8')
cursor = connect.cursor()

driverpath='/home/alexwang/chromedriver'
driver = webdriver.Chrome(driverpath)

brands = ['ASUS華碩','Acer宏碁','Lenovo聯想']

for brand in brands:
    url = 'https://tw.buy.yahoo.com/category/4385994?flt=品牌_{}'.format(brand)
    driver.get(url)
    
    for i in range(3):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)
    
    data = BeautifulSoup(driver.page_source, 'html.parser')
    items = data.find_all(class_='BaseGridItem__grid___2wuJ7 BaseGridItem__multipleImage___37M7b')
    
    for item in items:
        
        link=item.find('a').get('href')
        img=item.find('img').get('src')
        title=item.find('span', class_='BaseGridItem__title___2HWui').text
        price = item.find('em').text
        price = price.replace('$','')
        price = price.replace(',','')
        
        sql = "insert into shop(webname, title, price, link, photo, brand) values('yahoo','{}',{},'{}','{}','{}')".format(title, price, link, img, brand)
        cursor.execute(sql)
        connect.commit()
    
        
cursor.close()
connect.close()
driver.quit()
