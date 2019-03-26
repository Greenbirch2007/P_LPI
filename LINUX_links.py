# ! -*- coding:utf-8 -*-

import time
import re
import pymysql
import requests
from selenium import webdriver
# 还是要用PhantomJS
import datetime
import string
from lxml import etree




def call_pages(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    driver.close()
    return html

def parse_pages(html):
    big_list = []
    selector = etree.HTML(html)
    title = selector.xpath('//*[@id="arcs-list"]/li/a/text()')
    links = selector.xpath('//*[@id="arcs-list"]/li/a/@href')
    for i1,i2 in zip(title,links):
        big_list.append((i1,i2,"硬件·内核·Shell·监测"))

    return big_list



def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='LINUX',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    # 这里是判断big_list的长度，不是content字符的长度
    try:
        cursor.executemany('insert into linux_list1 (title,link,contents) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except Exception :
        print('出列啦')




if __name__ == '__main__':
    for num in range(1,5):
        url = 'http://man.linuxde.net/par/3/page/' + str(num)
        html = call_pages(url)
        content = parse_pages(html)
        insertDB(content)






# create table linux_list1 (
# id int not null primary key auto_increment,
# title varchar(100),
# link varchar(150),
# contents varchar(20)
# ) engine =InnoDB charset=utf8;
# #
# drop table linux_learning;




#





