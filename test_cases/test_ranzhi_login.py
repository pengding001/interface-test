#!/usr/bin/env python3.6.5
# encoding: utf-8  
# @Time    : 2018/6/24 14:40  
# @Author  : pengding  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : test_ranzhi_login.py  
# @Software: PyCharm


import re
import requests
import hashlib
import unittest

class testRanzhiLogin(unittest.TestCase):
    def setUp(self):
        self.url = ""
        self.username = "admin"
        self.password = "123456"
        pass

    def tearDown(self):
        pass

    def test_ranzhi_login(self):
        #1.请求登录页
        res = requests.get(self.url)
        #2.通过正则表达式获取v.random的值
        pattern = "(?=v.random = \").*(?=;<)"
        result = re.search(pattern, res.text).group()
        random_str = result.replace('v.random = "', '').replace('"','')
        #3.对password进行加密
        step1 = hashlib.md5(random_str.encode('utf-8')).hexdigest()
        tem1 = step1 + self.username
        step2 = hashlib.md5(tem1.encode('utf-8')).hexdigest()
        temp2 = step2 + random_str
        #4.构造请求参数
        #5.发送请求
        #6.校验结果
        r = requests.get()
        pass

if __name__ == "__main__":
    unittest.main