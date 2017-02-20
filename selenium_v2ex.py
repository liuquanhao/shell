#!/usr/bin/python

#-*- coding:utf-8 -*-

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

class V2exCoin():
    driver = None
    element = None
    cookies = None

    def __init__(self):
        self.driver = webdriver.PhantomJS(service_log_path='/dev/null')
        self.driver.get("https://www.v2ex.com/signin")
        self.login()

    def login(self):
        self.driver.find_element_by_xpath('//*[@id="Main"]/div[2]/div[2]/form/table/tbody/tr[1]/td[2]/input').send_keys("username")
        self.driver.find_element_by_xpath('//*[@id="Main"]/div[2]/div[2]/form/table/tbody/tr[2]/td[2]/input').send_keys("password")
        self.driver.find_element_by_xpath('//*[@id="Main"]/div[2]/div[2]/form/table/tbody/tr[3]/td[2]/input[2]').click()

    def get_coin(self):
        self.driver.get("https://www.v2ex.com/mission/daily")
        self.driver.find_element_by_xpath('//*[@id="Main"]/div[2]/div[2]/input').click()

if __name__ == "__main__":
        V2exCoin().get_coin()




