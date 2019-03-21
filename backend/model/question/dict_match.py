# -*- coding: utf-8 -*-
# File: dict_match.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-09


class DictMatch():
    @classmethod
    def dict_match(cls, question_str, dict_file_path):
        """
        字典匹配法抽取实体, 遵循最大匹配优先策略
        :param question_str:
        :param dict_file_path:
        :return:
        """
        dict_item_list = []
        with open(dict_file_path, 'r', encoding='utf8') as in_file:
            for line in in_file.readlines():
                if len(line.strip()) > 1:
                    dict_item_list.append(line.strip())
        dict_item_list.sort(key=lambda s: len(s), reverse=True)
        entity_list = []
        for dict_item in dict_item_list:
            if dict_item in question_str:
                question_str = question_str.replace(dict_item, '####')
                entity_list.append(dict_item)

        return entity_list


    @classmethod
    def room_dict_match(cls, question_str):
        """
        字典匹配的方式抽取馆室实体
        :return:
        """
        entity_list = cls.dict_match(question_str, '../../resource/room_list.txt')
        return entity_list

    @classmethod
    def resource_dict_match(cls, question_str):
        """
        字典匹配的方式抽取资源实体
        :return:
        """
        entity_list = cls.dict_match(question_str, '../../resource/resource_list.txt')
        return entity_list

    @classmethod
    def building_dict_match(cls, question_str):
        """
        字典匹配的方式抽取楼层实体
        :return:
        """
        entity_list = cls.dict_match(question_str, '../../resource/floor_list.txt')
        return entity_list






if __name__ == '__main__':
    pass




