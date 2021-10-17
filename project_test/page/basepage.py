import logging
import time

import yaml
from appium import webdriver
#from appium.webdriver import WebElement
#from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    _black_list = []
    _error_cont = 0
    _error_max = 10
    _param = {}
    _current_element: WebElement = None
    driver: WebDriver = None

    def __init__(self, _driver: WebDriver = None, _current_element: WebElement = None):
        self._driver = _driver
        self._current_element = _current_element

    def find(self, by, locator):
        """
        1. 定位元素
        2. 干掉弹窗
        3. 若弹窗不在黑名单内，则循环超过十次停止，防止死循环
        :param by: 定位方法
        :param locator: 定位元素
        :return: 定位
        """
        self._error_cont = 0
        try:
#            self._driver.find_element(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            self._driver.find_element()
            return self
        except Exception as e:
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()

    def send(self, value, by, locator):
        """
        1.防止弹窗是在搜索的时候弹出
        :param value: 搜索内容
        :param by: 定位方法
        :param locator: 定位元素
        :return: 定位
        """
        try:
            self.find(by, locator).send_keys(value)
            self._error_cont = 0
        except Exception as e:
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise e
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value, by, locator)

    def steps(self, path):
        """
        数据格式：
        - by :  id
            locator : search_input_text
            action : send
            value: "{value}"
            :param path: 路径
            :return: 根据数据进行操作
        - by : id
            locator: action_search
            action: click
        """
        with open(path, encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                    if "action" in step.keys():
                        if "click" == step["action"]:
                            element.click()
                        if "send" == step["action"]:
                            for param in self._param:
                                content = step["value"]
                                content: str = content.replace("{%s}" % param, self._param[param])
                                self.send(content, step["by"], step["locator"])

    def send_keys_(self, send_text):
        self._current_element = self._current_element.send_keys(send_text)
        return self

    def _click(self):
        self._current_element = self._current_element.click()
        return self

    def po_run(self, path, po_method, **kwargs):
        """
        yaml数据格式要求例如：
            search:
              - id: home_search
              - active: click
              - id: search_input_text
              - send_keys: alibaba
              - id: name
              - active: click
        :param path: yaml文件路径
        :param po_method:数据的方法名
        :return:根据给的定位元素进行操作，确定点击还是输入数据
        """
        with open(path)as f:
            yaml_data = yaml.safe_load(f)
            for step in yaml_data[po_method]:
                if isinstance(step, dict,):
                    for key in step.keys():
                        if key == "id":
                            self.find(By.ID, step[key])._click()

                    #     elif key == "click":
                    #         print("2222222")
                    #         self.click()
                    #     elif key == "send_keys":
                    #         print("点位send_keys111111111111111111111111111111")
                    #         text = str(step[key])
                    #         for k, v in kwargs.items():
                    #             real_text = text.replace("{' + k + '}", v)
                    #             self.send_keys(real_text)
                    # else:
                            logging.error(f"don't know {step}")

