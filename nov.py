#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zty
#  本代码实现爬取小说排行榜的所有小说并保存下来
import zty
import re
import requests
import time
def getBookUrl(webUrl):  # webUrl是指排行榜页面的地址  返回书本的地址列表
    webSoup = zty.getSoup(webUrl)
    bookUrls = webSoup.find('div',class_='main_m')
    op = []
    books = []
    for ea in bookUrls:
       url = re.findall(r'href="(/book/.*?)"',str(ea))
       op.append(url)  #op[1]里面是所有的地址  每一个地址会重复2遍 ，所以后面做了一下过滤   类型为list
    for num in range(0,len(op[3])):
        if num%2 == 0:
            books.append('https://www.bookbao99.net'+op[3][num])
    return books

if __name__ == '__main__':
    rs = list()
    webUrl = 'https://www.bookbao99.net/BookList-c_2-t_0-o_0.html'
    soup2 = zty.getSoup(webUrl)
    booknames = soup2.findAll('div', class_='bookname')
    bookname = re.findall(r'_blank">(.*?)</a>',str(booknames))
    print('以下是排行榜单：')
    for i in range(0,len(bookname)):
        print(str(i+1)+'. '+bookname[i], end=' ')
        if (i+1)%5==0 :
            print('\n')
    print('\n')
    id = input("请选择需要下载的小说编号，按回车键结束：")
    print('您选择的小说是：'+bookname[int(id)-1])
    # print("即将为您下载")
    bookurlist = getBookUrl(webUrl)
    booktitileurls = bookurlist[int(id)-1]
    downloadUrl = booktitileurls.replace('book','down').replace('down','book',1)  #获取下载页面链接
    soupDownload = zty.getSoup(downloadUrl)
    down = soupDownload.findAll('div',class_='info_buttondiv')
    downurl = re.findall(r'href="(.*?)" targe',str(down))
    finalUrl = downurl[0]
    print("开始下载，请稍候……")
    newfile = requests.get(finalUrl)
    checkFile = open(bookname[int(id)-1]+'.txt', "wb")
    for i in newfile.iter_content(100):
        checkFile.write(i)
    print("下载完成，即将退出")
    time.sleep(3)





