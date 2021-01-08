#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
类中基础方法测试
'''
import unittest
from shoppingcart import ShoppingCart

class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        self.shcart = ShoppingCart()

    def test_deal_discount(self):
        self.shcart.add_discount(['2013.11.11 | 0.7 | 电子'])
        ret = self.shcart.deal_discount()
        self.assertEqual(ret, {'电子': ['2013.11.11', 0.7]})

    def test_deal_coupons(self):
        self.shcart.add_coupon(['2014.3.2 1000 200', '1999.3.2 2000 500',
                                '2014.5.2 500 50', '2014.3.12 5000 1500'])
        self.shcart.set_paydate('2013.11.11')
        rets = []
        rets.append(self.shcart.deal_coupons(400))
        rets.append(self.shcart.deal_coupons(1500))
        rets.append(self.shcart.deal_coupons(3000))
        self.assertEqual(rets, [0, 200, 200])

    def test_compare_date(self):
        rets = []
        rets.append(self.shcart.compare_date('2014.3.2', '2013.11.11'))
        rets.append(self.shcart.compare_date('2014.3.2', '2014.3.2'))
        rets.append(self.shcart.compare_date('2014.3.2', '2015.11.11'))
        self.assertEqual(rets, [1, 0, -1])

    def test_add_discount(self):
        self.shcart.add_discount(['2013.11.11 | 0.7 | 电子'])
        self.assertEqual(self.shcart.discount_info, ['2013.11.11 | 0.7 | 电子'])

    def test_add_goods(self):
        goods = ['1 * ipad : 2399.00', '1 * 显示器 : 1799.00', '12 * 啤酒 : 25.00',
                 '5 * 面包 : 9.00']
        self.shcart.add_goods(goods)
        self.assertEqual(self.shcart.goods_info, goods)

    def test_set_paydate(self):
        self.shcart.set_paydate('2013.11.11')
        self.assertEqual(self.shcart.pay_date, '2013.11.11')

    def test_add_coupon(self):
        self.shcart.add_coupon(['2014.3.2 1000 200'])
        self.assertEqual(self.shcart.coupons, ['2014.3.2 1000 200'])

if __name__ == '__main__':
    unittest.main()