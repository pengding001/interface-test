#!/usr/bin/env python3.6.5
# encoding: utf-8  
# @Time    : 2018/6/24 16:45  
# @Author  : pengding  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : historyweather_suite.py  
# @Software: PyCharm


import unittest
from test_cases.test_histroyweather import testHistory

def history_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(testHistory))
    return suite
