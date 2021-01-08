#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import logging
from config import Config


class Log:
    today = time.strftime("%Y-%m-%d",time.localtime(time.time()))
    logpath = os.path.join(Config.log_path, today+ '.log')

    logger = logging.getLogger('log')
    logger.setLevel(logging.DEBUG)

    # file log 写入文件配置
    formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # 日志的格式
    fh = logging.FileHandler(logpath, encoding='utf-8')  # 日志文件路径文件名称，编码格式
    fh.setLevel(logging.DEBUG)  # 日志打印级别
    fh.setFormatter(formatter)
    logger.addHandler(fh)


log = Log()
