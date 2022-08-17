import unittest
from tools import HTMLTestRunner
from test1 import Test1

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Test1))

with open("./reports/test1_login_test_report.html", "wb") as f:
    h = HTMLTestRunner.HTMLTestRunner(stream=f, title="测试报告", description='windows 10')
    h.run(suite)