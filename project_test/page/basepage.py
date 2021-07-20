import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:

    _black_list = []
    _error_cont = 0
    _error_max = 10
    _param = {}

    def __init__(self, _driver: WebDriver = None):
        self._driver = _driver

    def find(self, by, locator):
        """
        1. 定位元素
        2. 干掉弹窗
        3. 若弹窗不在黑名单内，则循环超过十次停止，防止死循环
        :param by: 定位方法
        :param locator: 定位元素
        :return: 定位
        """
        try:
            element = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.\
                find_element(by, locator)
            return element
            self._error_cont = 0
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
        with open(path, encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
            print(steps)
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
                                self.send(content, step["by"],step["locator"])
