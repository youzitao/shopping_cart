#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Email:522174316@qq.com

import sys
import traceback
from config import Config
from makelog import log

class Goods:
    '''
    已上架商品信息
    '''
    def __init__(self, goodspath):
        self.goods_category = {}  # 商品类别标签 {'ipad':'电子'}
        self.init(goodspath)


    def init(self,filepath):
        '''
        初始化仓库信息
        :param filepath:
        :return:
        '''
        try:
            if sys.version.startswith('2.'):
                fileobj = open(filepath)
            else:
                fileobj = open(filepath, encoding='utf-8')
            for eachline in fileobj:
                eachline = eachline.replace('：', ':').replace('，', ',')
                if eachline.strip():
                    cate, goods = eachline.strip().split(':')
                    self.goods_category.update(
                        {each.strip(): cate for each in goods.split(',')})
        except:
            log.logger.error("init()_fail_%s"%filepath)
            log.logger.error(traceback.format_exc())
        finally:
            if fileobj:
                fileobj.close()

    def add_goods_category(self, goods_dic):
        '''
        添加、更新商品类别
        :param goods_dic: {'商品名称':'类别'}
        '''
        self.goods_category.update(goods_dic)

    def get_category(self, name):
        '''
        获取商品类别
        :param name:
        :return:
        '''
        return self.goods_category.get(name, '')

goods = Goods(Config.products_path)

if __name__ == '__main__':
    print(goods.goods_category)

