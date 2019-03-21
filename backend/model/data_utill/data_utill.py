# -*- coding: utf-8 -*-
# File: data_utill.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-09
import os
import sys
# 模块路径引用统一回退到Libbot目录下
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)



class DataUtill():
    """
    一些常用数据处理工具类
    """
    @classmethod
    def load_plain_list(cls, file_path):
        """
        从一些文本中加载逐行存储的列表元素
        :return:
        """
        res_list = []
        try:
            with open(file_path, 'r', encoding='utf8') as in_file:
                for line in in_file.readlines():
                    res_list.append(line.strip())
        except Exception as e:
            print('Fail to load data from '+file_path)
            print(e)
            return None
        return res_list



if __name__=='__main__':
    pass