# -*- coding: utf-8 -*-
# File: entity_match.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-20
import os
import sys
# 模块路径引用统一回退到Libbot目录下
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)

from model.question.dict_match import DictMatch

replace_entity_mark = {
    'room': 'ROOM',
    'resource': 'RES',
    'floor': 'FLOOR',
    'business': 'BUS',
    'people': 'PEOPLE',
    'card': 'CARD',
    'condition': 'COND'
}

class entityMatch():
    """
    对问句中地实体进行匹配、抽取、替换
    """
    @classmethod
    def room_dict_match(cls, question_str):
        """
        字典匹配的方式抽取馆室实体,并替换为特殊实体标记
        :return:
        """
        entity_list = DictMatch.dict_match(question_str, '../../resource/room_list.txt')
        for entity in entity_list:
            question_str = question_str.replace(entity, replace_entity_mark['room'])
        return question_str, entity_list


    @classmethod
    def resource_dict_match(cls, question_str):
        """
        字典匹配的方式抽取资源实体
        :return:
        """
        entity_list = DictMatch.dict_match(question_str, '../../resource/resource_list.txt')
        for entity in entity_list:
            question_str = question_str.replace(entity, replace_entity_mark['resource'])
        return question_str, entity_list

    @classmethod
    def floor_dict_match(cls, question_str):
        """
        字典匹配的方式抽取楼层实体
        :return:
        """
        entity_list = DictMatch.dict_match(question_str, '../../resource/floor_list.txt')
        for entity in entity_list:
            question_str = question_str.replace(entity, replace_entity_mark['floor'])
        return question_str, entity_list


    @classmethod
    def match_and_replace_all(cls, question_str):
        """
        对问句进行所有类型实体匹配与替换
        :param question_str:
        :return:
        """
        entity_dict = {}  # 分类存放匹配到的各类实体
        question_str, entity_list = cls.room_dict_match(question_str)
        entity_dict['room'] = entity_list
        question_str, entity_list = cls.resource_dict_match(question_str)
        entity_dict['res'] = entity_list
        question_str, entity_list = cls.resource_dict_match(question_str)
        entity_dict['floor'] = entity_list

        return question_str, entity_dict



