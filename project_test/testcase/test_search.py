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
import pytest

from project_test.page.app import App
from project_test.page.search_modle import SearchModule
from project_test.page.utils import Utils

# todo：数据驱动


class TestSearch:
    data = Utils.from_file("../config/test_search.yaml", "search")

    def setup_class(self):
        self.App = App()
        self.App.start()
        self.SearchModule = SearchModule()

    def teardown_teardown(self):
        pass
    # self.App.stop()


    @pytest.mark.parametrize('keyword', data["values"])
    def test_search(self, keyword):
        self.SearchModule.search_module(keyword)



