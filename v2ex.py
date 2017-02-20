#!/usr/bin/python
#-*- coding:utf-8 -*-

import requests
from lxml import etree
import re

class V2exCoin():
    s = None
    url = "https://www.v2ex.com"
    login_url = url + '/signin'
    user_key = None
    password_key = None
    once_code = None

    def __init__(self):
        self.s = requests.Session()
        self.get_key()
        self.login()

    def get_key(self):
        response = self.s.get(self.login_url)
        html = etree.HTML(response.text)
        self.user_key = html.xpath('//input[@class="sl"]')[0].attrib['name']
        self.password_key = html.xpath('//input[@class="sl"]')[1].attrib['name']
        self.once_code = html.xpath('//form/table//input[@type="hidden"]')[0].attrib['value']

    def login(self):
        payload = {
            self.user_key:'username',
            self.password_key:'password',
            'once':self.once_code,
            'next':'/'
        }
        headers = {
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'referer':'https://www.v2ex.com/signin'
        }
        self.s.post(self.login_url,data=payload,headers=headers)

    def get_coin(self):
        r = self.s.get("https://www.v2ex.com/mission/daily")
        html = etree.HTML(r.text)
        js = html.xpath('//div[@class="cell"]/input')[0].attrib['onclick']
        coin_url = re.findall(r'(/miss.*\d+)',js)
        if coin_url != []:
            self.s.get(self.url + coin_url[0])

if __name__ == "__main__":
        V2exCoin().get_coin()




