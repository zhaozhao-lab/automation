#!/usr/bin/env python
# encoding: utf-8
from project_test.page.basepage import BasePage


class Search(BasePage):
    def search(self, value):
        self._param["value"] = value
        self.steps("../page/search.yaml")