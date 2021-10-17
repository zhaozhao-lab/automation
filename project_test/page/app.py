#!/usr/bin/env python
# encoding: utf-8
from appium import webdriver
from project_test.page.basepage import BasePage


class App(BasePage):
    def start(self):     # 启动app
        _appPackage = "com.xueqiu.android"
        _appActivity = ".view.WelcomeActivityAlias"
        if self._driver is None:
            desire_cap = {
                "platformName": "Android",
                "devicesName": "127.0.0.1:62001",
                "appPackage": _appPackage,
                "noReset": "true",
                "appActivity": _appActivity,
                #"dontStopAppOnReset": "true"
            }
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", desire_cap)
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity(_appActivity, _appPackage)
        return self

    def stop(self):
        self._driver.quit()

