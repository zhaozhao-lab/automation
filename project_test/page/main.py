#!/usr/bin/env python
# encoding: utf-8

from project_test.page.basepage import BasePage
from project_test.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")

        return Market(self._driver)