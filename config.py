#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
项目配置文件
'''

import os

class Config:
    # 项目所目录
    base_path = os.path.split(os.path.realpath(__file__))[0]
    # 产品目录文件路径
    products_path = os.path.join(base_path, 'products')
    # log路径
    log_path = os.path.join(base_path, 'log')
    # 测试文件路径
    test_data_path = os.path.join(base_path, 'test', 'test_data')

