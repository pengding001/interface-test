#!/usr/bin/env python3.6.5
# encoding: utf-8  
# @Time    : 2018/6/24 16:53  
# @Author  : pengding  
# @contact: xxxx@qq.com  
# @Site    :   
# @File    : run.py  
# @Software: PyCharm


import unittest
import HTMLReport
from test_suites import historyweather_suite

if __name__ == "__main__":

# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTests(historyweather_suite.history_suite())

#test_suites
    HTMLReport.TestRunner(
        report_file_name="",
        title="历史天气测试",
        log_file_name="历史天气测试.log",
        thread_count=3
    ).run(historyweather_suite.history_suite())
