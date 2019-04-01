# -*- coding: utf-8 -*-
# File: entity_match2.py
# Author: Liu liting <nkliuliting826@mail.nankai.edu.cn>
# CreateDate: 19-03-30

import os
import sys
from model.question.dict_match2 import DictMatch2
from model.kb_prepare.rdf_prepare import rdfPrepare
import time

# 模块路径引用统一回退到Libbot目录下
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)

replace_entity_mark = {
    'room': 'ROOM',
    'resource': 'RES',
    'floor': 'FLOOR',
    'business': 'BUS',
    'people': 'PEOPLE',
    'card': 'CARD',
    'condition': 'COND'
}

class entityMatch2():
    """
    对问句中地实体进行匹配、抽取、替换
    """
    @classmethod
    def room_dict_match(cls, question_str, var_list, graph):
        dict_list = rdfPrepare.rdf_query_varientnames('room', graph)
        entities = DictMatch2.room_dict_match(question_str, var_list, graph)
        if (len(entities) != 0):
            entities = entities[0]
        for entity in entities:
            for varname in dict_list[entity]:
                question_str = question_str.replace(varname, replace_entity_mark['room'])
        return question_str, entities

    @classmethod
    def resource_dict_match(cls, question_str, var_list, graph):
        dict_list = rdfPrepare.rdf_query_varientnames('resource', graph)
        entities = DictMatch2.resource_dict_match(question_str,var_list, graph)
        if (len(entities) != 0):
            entities = entities[0]
        for entity in entities:
            for varname in dict_list[entity]:
                question_str = question_str.replace(varname, replace_entity_mark['resource'])
        return question_str, entities

    @classmethod
    def floor_dict_match(cls, question_str,var_list, graph):
        dict_list = rdfPrepare.rdf_query_varientnames('floor', graph)
        entities = DictMatch2.floor_dict_match(question_str,var_list, graph)
        if (len(entities) != 0):
            entities = entities[0]
        for entity in entities:
            for varname in dict_list[entity]:
                question_str = question_str.replace(varname, replace_entity_mark['floor'])
        return question_str, entities

    @classmethod
    def match_and_replace_all(cls, question_str, graph):
        """
        对问句进行所有类型实体匹配与替换
        :param question_str:
        :return:
        """
        entity_dict = {} #分类存放匹配到的各类实体
        var_list = DictMatch2.var_dict_list(graph)
        question_str, entity_list = cls.room_dict_match(question_str,var_list, graph)
        entity_dict['room'] = entity_list
        question_str, entity_list = cls.resource_dict_match(question_str,var_list, graph)
        entity_dict['res'] = entity_list
        question_str, entity_list = cls.floor_dict_match(question_str,var_list, graph)
        entity_dict['floor'] = entity_list
        return question_str,entity_dict

# if __name__=="__main__":
#     g = rdfPrepare.load_graph()
#     question_str, entity_list = entityMatch2.match_and_replace_all("少年儿童馆数字资源体验区的电话是啥？",g)
#     print(question_str)
#     print(entity_list)