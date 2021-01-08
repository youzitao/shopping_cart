#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import unittest
from decimal import Decimal, ROUND_HALF_UP
from shoppingcart import ShoppingCart
from config import Config
from run import deal_file

class ShoppingCartTest(unittest.TestCase):
    '''
    Case A : 题目用例，有促销，有优惠券
    Case B : 题目用例，无促销，无优惠券
    Case 3 : 促销信息与结算日期不在同一天，不享受促销优惠
    Case 4 : 没有促销活动，有优惠券，但优惠券过期
    Case 5 : 有促销活动，有优惠券，但优惠券过期
    Case 6 : 多个促销活动
    Case 7 : 多张优惠券，含过期
    Case 8 : 购物车没有商品
    # 信息异常时
    Case 9 : 促销信息不全，则此类产品不进行优惠
    Case 10 : 优惠券信息不全，此张优惠券无效
    '''

    def setUp(self):
        self.shcart = ShoppingCart()

    def test_start_settlement_1(self):
        '''
        Case  A
        题目用例，有促销，有优惠券
        :return:
        '''
        case_path = os.path.join(Config.test_data_path, 'case_A.txt')
        allinfo = deal_file(case_path)
        self.shcart.add_discount(allinfo[0])
        self.shcart.add_goods(allinfo[1])
        self.shcart.set_paydate(allinfo[2][0])
        self.shcart.add_coupon(allinfo[3])
        ret = self.shcart.start_settlement()
        self.assertEqual(ret, Decimal(3083.60).quantize(Decimal('0.00'),
                                                  rounding=ROUND_HALF_UP))

    def test_start_settlement_2(self):
        '''
        Case  B
        题目用例，无促销，无优惠券
        :return:
        '''
        case_path = os.path.join(Config.test_data_path, 'case_B.txt')
        allinfo = deal_file(case_path)
        self.shcart.add_discount(allinfo[0])
        self.shcart.add_goods(allinfo[1])
        self.shcart.set_paydate(allinfo[2][0])
        self.shcart.add_coupon(allinfo[3])
        ret = self.shcart.start_settlement()
        ret = self.shcart.start_settlement()
        self.assertEqual(ret, Decimal(43.54).quantize(Decimal('0.00'),
                                                  rounding=ROUND_HALF_UP))

    def test_start_settlement_3(self):
        '''
        Case  3
        促销信息与结算日期不在同一天，不享受促销优惠
        :return:
        '''
        case_path = os.path.join(Config.test_data_path, 'case_3.txt')
        allinfo = deal_file(case_path)
        self.shcart.add_discount(allinfo[0])
        self.shcart.add_goods(allinfo[1])
        self.shcart.set_paydate(allinfo[2][0])
        self.shcart.add_coupon(allinfo[3])
        ret = self.shcart.start_settlement()
        ret = self.shcart.start_settlement()
        self.assertEqual(ret, Decimal(4043.00).quantize(Decimal('0.00'),
                                                  rounding=ROUND_HALF_UP))

    def test_start_settlement_4(self):
        '''
        Case  4
        没有促销活动，有优惠券，但优惠券过期
        :return:
        '''
        case_path = os.path.join(Config.test_data_path, 'case_4.txt')
        allinfo = deal_file(case_path)
        self.shcart.add_discount(allinfo[0])
        self.shcart.add_goods(allinfo[1])
        self.shcart.set_paydate(allinfo[2][0])
        self.shcart.add_coupon(allinfo[3])
        ret = self.shcart.start_settlement()
        ret = self.shcart.start_settlement()
        self.assertEqual(ret, Decimal(4543.00).quantize(Decimal('0.00'),
                                                  rounding=ROUND_HALF_UP))

    def test_start_settlement_5(self):
        '''
        Case  5
        有促销活动，有优惠券，但优惠券过期
        :return:
        '''
        case_path = os.path.join(Config.test_data_path, 'case_5.txt')
        allinfo = deal_file(case_path)
        self.shcart.add_discount(allinfo[0])
        self.shcart.add_goods(allinfo[1])
        self.shcart.set_paydate(allinfo[2][0])
        self.shcart.add_coupon(allinfo[3])
        ret = self.shcart.start_settlement()
        ret = self.shcart.start_settlement()
        self.assertEqual(ret, Decimal(4393.00).quantize(Decimal('0.00'),
                                                  rounding=ROUND_HALF_UP))

    def test_start_settlement_6(self):
        '''
        Case  6
        多个促销活动
        :return:
        '''
        case_path = os.path.join(Config.test_data_path, 'case_6.txt')
        allinfo = deal_file(case_path)
        self.shcart.add_discount(allinfo[0])
        self.shcart.add_goods(allinfo[1])
        self.shcart.set_paydate(allinfo[2][0])
        self.shcart.add_coupon(allinfo[3])
        ret = self.shcart.start_settlement()
        ret = self.shcart.start_settlement()
        self.assertEqual(ret, Decimal(2924.60).quantize(Decimal('0.00'),
                                                  rounding=ROUND_HALF_UP))

    def test_start_settlement_7(self):
        '''
        Case  7
        多张优惠券，含过期
        :return:
        '''
        case_path = os.path.join(Config.test_data_path, 'case_7.txt')
        allinfo = deal_file(case_path)
        self.shcart.add_discount(allinfo[0])
        self.shcart.add_goods(allinfo[1])
        self.shcart.set_paydate(allinfo[2][0])
        self.shcart.add_coupon(allinfo[3])
        ret = self.shcart.start_settlement()
        ret = self.shcart.start_settlement()
        self.assertEqual(ret, Decimal(2624.60).quantize(Decimal('0.00'),
                                                  rounding=ROUND_HALF_UP))

    def test_start_settlement_8(self):
        '''
        Case  8
        购物车没有商品
        :return:
        '''
        case_path = os.path.join(Config.test_data_path, 'case_8.txt')
        allinfo = deal_file(case_path)
        self.shcart.add_discount(allinfo[0])
        self.shcart.add_goods(allinfo[1])
        self.shcart.set_paydate(allinfo[2][0])
        self.shcart.add_coupon(allinfo[3])
        ret = self.shcart.start_settlement()
        ret = self.shcart.start_settlement()
        self.assertEqual(ret, Decimal(0.00).quantize(Decimal('0.00'),
                                                  rounding=ROUND_HALF_UP))

    def test_start_settlement_9(self):
        '''
        Case  9
        促销信息不全，则此类产品不进行优惠
        :return:
        '''
        case_path = os.path.join(Config.test_data_path, 'case_9.txt')
        allinfo = deal_file(case_path)
        self.shcart.add_discount(allinfo[0])
        self.shcart.add_goods(allinfo[1])
        self.shcart.set_paydate(allinfo[2][0])
        self.shcart.add_coupon(allinfo[3])
        ret = self.shcart.start_settlement()
        ret = self.shcart.start_settlement()
        self.assertEqual(ret, Decimal(300.00).quantize(Decimal('0.00'),
                                                  rounding=ROUND_HALF_UP))

    def test_start_settlement_10(self):
        '''
        Case  10
        优惠券信息不全，此张优惠券无效
        :return:
        '''
        case_path = os.path.join(Config.test_data_path, 'case_10.txt')
        allinfo = deal_file(case_path)
        self.shcart.add_discount(allinfo[0])
        self.shcart.add_goods(allinfo[1])
        self.shcart.set_paydate(allinfo[2][0])
        self.shcart.add_coupon(allinfo[3])
        ret = self.shcart.start_settlement()
        ret = self.shcart.start_settlement()
        self.assertEqual(ret, Decimal(4393.00).quantize(Decimal('0.00'),
                                                  rounding=ROUND_HALF_UP))

if __name__ == '__main__':
    unittest.main()


