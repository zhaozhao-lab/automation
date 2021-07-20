#!/usr/bin/env python
# encoding: utf-8
'''
@author:zhaolong
@contact: 1452885022@qq.com
@software: laka
@file: test_search.py
@time: 2021/7/20 18:28
@desc:
'''
from project_test.page.app import App


class TestSearch:
    def test_search(self):
        App().start().main().goto_market().goto_search().search("jingdong")