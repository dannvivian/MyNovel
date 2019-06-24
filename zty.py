#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zty
import requests
import re
from bs4 import BeautifulSoup
def  getSoup(web_url)  :
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    req = requests.get(web_url,headers=headers)
    req.encoding = req.apparent_encoding
    Soup = BeautifulSoup(req.text, 'lxml')
    return Soup
if __name__  == '__main__' :
    {}

