#!/usr/bin/env python
# encoding: utf-8

from project_test.page.basepage import BasePage
from project_test.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)
