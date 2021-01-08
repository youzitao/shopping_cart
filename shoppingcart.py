#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import traceback
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime
from warehouse import goods
from makelog import log

class ShoppingCart:
    '''
    购物车
    '''

    def __init__(self):
        self.discount_info = []    # 促销信息
        self.goods_info = []       # 购物车商品
        self.pay_date = ''         # 结算日期
        self.coupons = []          # 优惠券列表


    def add_discount(self, discount):
        '''
        增加折扣信息
        :param discount:促销列表，[2013.11.11 | 0.7 | 电⼦,...]
        '''
        self.discount_info.extend(discount)

    def add_goods(self, goods):
        '''
        购物车添加商品
        :param goods:商品列表，[1 * ipad : 2399.00,...]
        '''
        self.goods_info.extend(goods)

    def set_paydate(self, paydate):
        '''
        设置结算日期
        :param paydate:结算日期，2014.01.01
        '''
        self.pay_date = paydate

    def add_coupon(self, coupon):
        '''
        添加优惠券
        :param coupon:优惠券列表，[2014.3.2 1000 200, ...]
        '''
        self.coupons.extend(coupon)


    def deal_discount(self):
        '''
        处理促销信息
        :return:self.discount_dic ， {'电⼦':['2013.11.11', 0.7], ...}
        '''
        discount_dic = {}
        for each_info in self.discount_info:
            try:
                dis_date, dis_rate, dis_category = each_info.split('|')
                if dis_date and dis_rate and dis_category:
                    discount_dic[dis_category.strip()] = [dis_date.strip(),
                                                    float(dis_rate.strip())]
            except:
                log.logger.error('deal_discount()_%s'%each_info)
                log.logger.error(traceback.format_exc())
        return discount_dic


    def deal_coupons(self, total):
        '''
        处理优惠券,多张优惠券，根据总价优先返回折扣最大的一张
        :param total:总价
        :return:，max_dis 折扣额度
        '''
        coupons_dic = {}
        for each in self.coupons:
            try:
                cou_date, sum_pic,dis_pic = each.split(' ')
                if self.compare_date(cou_date, self.pay_date) is 1:
                    coupons_dic.setdefault(float(sum_pic), float(dis_pic))
            except:
                log.logger.error('deal_coupons()_%s' % each)
                log.logger.error(traceback.format_exc())
        max_dis = coupons_dic.get(total, 0)
        if max_dis is 0: # 没有正好满足优惠券的价格
            sum_pics = list(coupons_dic.keys())
            sum_pics.append(total)
            sum_pics.sort()
            if total != sum_pics[0]:
                max_dis = coupons_dic.get(sum_pics[sum_pics.index(total)-1], 0)
        return max_dis

    def compare_date(self, datea, dateb):
        '''
        比较日期大小
        :param datea:
        :param datab:
        :return:
        '''
        d1 = datetime.strptime(datea, '%Y.%m.%d')
        d2 = datetime.strptime(dateb, '%Y.%m.%d')
        if d1 > d2:
            return 1
        elif d1 == d2:
            return 0
        else:
            return -1

    def start_settlement(self):
        '''
        开始结算
        :return:
        '''
        total = 0
        # 获取促销信息
        if self.pay_date:
            discount_dic = self.deal_discount()
            for eachinfo in self.goods_info:
                try:
                    num, name, price = re.findall('(\d+) \* (.*?) : (\d+\.\d+)', eachinfo)[0]
                    all_price = int(num) * float(price)
                    # 获取商品类别
                    category = goods.get_category(name)
                    cat_infos = discount_dic.get(category, [])
                    # 此类商品结算日是否促销
                    if cat_infos and self.compare_date(self.pay_date,cat_infos[0]) is 0:
                        all_price = all_price*cat_infos[1]
                    total += all_price
                except:
                    log.logger.error('start_settlement()_%s' % eachinfo)
                    log.logger.error(traceback.format_exc())

            max_dis = self.deal_coupons(total)
            total = total - max_dis
        return Decimal(total).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)
