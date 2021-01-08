#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Email:522174316@qq.com

import os
import sys
import traceback
from shoppingcart import ShoppingCart
from makelog import log
from config import Config

def deal_file(filepath):
    '''
    处理输入的文件信息
    :return:
    '''
    allinfo = [[], [], [], []]  # 促销信息，所购产品，结算日期，优惠券
    fileobj = None
    try:
        if sys.version.startswith('2.'): # python 2
            fileobj = open(filepath)
        else:
            fileobj = open(filepath, encoding='utf-8') # python 3
        data = fileobj.readlines()
        idx = 0
        for each in data:
            if allinfo[2] and not allinfo[3]:
                idx += 1
            if each.strip():
                allinfo[idx].append(each.strip())
            else:
                idx += 1
    except:
        log.logger.error('deal_file()_%s' % filepath)
        log.logger.error(traceback.format_exc())
    finally:
        if fileobj:
            fileobj.close()

    return allinfo

if __name__ == '__main__':
    filepath = os.path.join(Config.base_path,'test' ,'test_data', 'case_A.txt') # test
    # filepath = r''  # 添加文件路径或者使用命令行方式输入文件（第一个参数）
    if len(sys.argv) < 2 and not filepath:
        print('缺少文件路径参数!')
    else:
        if len(sys.argv) > 1:
            filepath = sys.argv[1]
        allinfo = deal_file(filepath)
        shcart = ShoppingCart()
        shcart.add_discount(allinfo[0])
        shcart.add_goods(allinfo[1])
        if allinfo[2]:
            shcart.set_paydate(allinfo[2][0])
        shcart.add_coupon(allinfo[3])
        print(shcart.start_settlement())




