import requests
from bs4 import BeautifulSoup
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='password', database='django', charset='utf8')
cursor = conn.cursor()

url='https://supertaste.tvbs.com.tw/topic/22'

content = requests.get(url).text
soup = BeautifulSoup(content, 'html.parser')
allData = soup.find('div', id='combolistUl')
data = allData.find_all('li')

domain='https://supertaste.tvbs.com.tw'
    
link=''
title=''
img=''
datetime=''
    
for row in data:
    link = domain + row.find('a').get('href')
    title = row.find('div', class_='txt').text
    img = row.find('img').get('data-original')
    datetime = row.find('div', class_='time').find('p').text
    
    sql = "insert into food(link, title, image, datetime) values('{}','{}','{}','{}')".format(link, title, img, datetime)
    cursor.execute(sql)
    conn.commit()
    
cursor.close()
conn.close()
    
#print(link)
#print(title)
#print(img)
#print(datetime)


