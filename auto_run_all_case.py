#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
自动测试所有用例
'''

import os
import sys
import time
import unittest

from config import Config
if sys.version.startswith('2.'):
    from libs import HTMLTestRunner
else:
    from libs import HTMLTestRunner3 as HTMLTestRunner

sys.path.append(Config.base_path)


def all_case():
    # 测试用例路径
    case_path = os.path.join(Config.base_path, 'test', 'test_case')
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    return discover

if __name__ == "__main__":

    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 报告存放路径
    report_path = os.path.join(Config.base_path, 'test','test_report')
    report_abspath = os.path.join(report_path, "Test_Result_" + now + ".html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'Shopping cart Test Report：',
                                           description=u'case information：')
    runner.run(all_case())
    fp.close()