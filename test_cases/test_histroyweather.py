#!/usr/bin/env python3.6.5
# encoding: utf-8  
# @Time    : 2018/6/24 15:56  
# @Author  : pengding  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : test_histroyweather.py  
# @Software: PyCharm

import unittest
import requests
from config import config


class testHistory(unittest.TestCase):
    def setUp(self):
        self.key = config.appkey
        self.province_url = config.confighost + "province"
        self.citys_url = config.confighost + "citys"
        self.weather_url = config.confighost + "weather"
        pass

    def tearDown(self):
        pass

    #获取省份列表信息
    def test_001province_list(self):
        param = {"key":self.key}
        res = requests.get(self.province_url, param)
        jsonRse = res.json()
        self.assertIn(jsonRse.get('reason'), "查询成功")

    #获取省份列表信息
    def test_002citys_list(self):
        param = {"key":self.key, "province_id":"1"}
        res = requests.post(self.citys_url, data=param)
        jsonRse = res.json()
        self.assertIn(jsonRse.get('reason'), "查询成功")

    #获取省份列表信息
    def test_003historyweather_list(self):
        param = {"key":self.key, "city_id":"255", "weather_date":"2018-06-23"}
        res = requests.post(self.weather_url, data=param)
        jsonRse = res.json()
        self.assertIn(jsonRse.get('reason'), "查询成功")

if __name__ == "__main__":
    unittest.main