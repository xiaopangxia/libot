# -*- coding: utf-8 -*-
# File: multiwheel_manage.py
# Author: LG
# CreateDate: 19-04-09

def _init():#初始化
    global _user_dict
    _user_dict = {}


def set_value(key,value):
    """ 定义一个全局变量 """
    _user_dict[key] = value


def get_value(key,defValue=None):
    try:
        return _user_dict[key]
    except KeyError:
        return defValue