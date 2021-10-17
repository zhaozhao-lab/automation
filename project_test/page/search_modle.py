#!/usr/bin/env python
# encoding: utf-8
"""
@author:ZhaoLong
@contact: 1452885022@qq.com
@software: Laka
@file: search_modle.py
@time: 2021/8/4 16:09
@desc:
"""
from project_test.page.basepage import BasePage
from project_test.page.utils import Utils


class SearchModule(BasePage):

    def search_module(self, keyword):
        self.po_run("../config/procedure.yml", "search", keyword=keyword)

