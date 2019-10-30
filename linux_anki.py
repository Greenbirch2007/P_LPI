
# -*- coding:utf-8 -*-
import datetime
import re
import time

import pymysql

from lxml import etree
from selenium import webdriver

driver = webdriver.Chrome()


def get_first_page(url):

    driver.get(url)
    html = driver.page_source
    return html



# 可以尝试第二种解析方式，更加容易做计算
def parse_note(html):
    try:

        big_list = []

        selector = etree.HTML(html)


        descs = selector.xpath('//*[@id="arc-body"]/p[1]/text()')
        # 遍历一个列表中的字符串，去字符串最长的那个字符串添加入big_list作为唯一的字符串
        max_str = max(descs, key=len)
        big_list.append(max_str)
        return big_list

    except ValueError as e:
        pass














def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='LINUX',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into linux_list2 (title,descs,contents) values (%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass




if __name__ == '__main__':

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='LINUX',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()
    #sql 语句
    for num in range(464,586):
        big_list = []
        sql = 'select * from linux_list1 where id = %s ' % num
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()  #字段名有３个　title,link,contents

        db_link = data["link"]
        db_title = data["title"]
        db_contents = data["contents"]
        big_list.append(db_title)
        big_list.append(db_contents)
        html = get_first_page(db_link)
        content = parse_note(html)
        for item in content:

            big_list.append(item)

        big_list_tuple = tuple(big_list)
        f_list = []
        f_list.append(big_list_tuple)
        insertDB(f_list)










# 因为板块数据是最后嵌套进去的，所以要保持，１．数据库表结构，２．解析整理后的数据结构　３．　插入的字段结构　三者之间都要保持一致
# create table linux_list2 (
# id int not null primary key auto_increment,
# title varchar(50),
# descs text,
# contents text
# ) engine =InnoDB charset=utf8;


# drop table linux_list2;