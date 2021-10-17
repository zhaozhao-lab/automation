#!/usr/bin/env python
# encoding: utf-8
"""
@author:zhaolong
@contact: 1452885022@qq.com
@software: laka
@file: utils.py
@time: 2021/8/2 19:14
@desc:
"""
from string import Template

import yaml


class Utils:
    @classmethod
    def from_file(cls, path, params):
        """
        读取yaml数据，提取数据的键值

        yaml文件格式要求：字典格式（不支持列表格式），数据为键值对，不为键值对会被过滤掉，去重（值是惟一的，相通的被过滤掉了）
        :param path: 读取yaml数据的路径
        :param params: 读取数据内要用的数据的数据名
        :return:数据的键值对
        """
        with open(path) as f:
            yaml_data = yaml.safe_load(f)
            params = yaml_data[params]
            keys = set()
            values = []
            if isinstance(params, list):
                for row in params:
                    if isinstance(row, dict):
                        for key in row.keys():
                            keys.add(key)
                            values.append(list(row.values()))
            var_names = ",".join(keys)
            return {"keys": var_names, "values": values}
# f = Utils()
# f = f.from_file("../config/test_search.yaml", "search")
# print(f["values"], str(f["values"]))
# print(f["keys"], type(f["keys"]))
#
