# -*- coding: utf-8 -*-
# File: dict_match2.py
# Author: Liu liting <nkliuliting826@mail.nankai.edu.cn>
# CreateDate: 19-03-30

from model.kb_prepare.rdf_prepare import rdfPrepare
import time

class DictMatch2():
    @classmethod
    def dict_match(cls, question_str, dict_list,type,graph):
        """
        字典匹配法抽取实体, 遵循最大匹配优先策略,匹配rdf返回的异名表
        :param question_str:
        :param dict_list:
        :return:
        """
        dict_list.sort(key=lambda s:len(s), reverse=True)
        entity_list = []
        var_list = [ ]
        for dict_item in dict_list:
            if dict_item in question_str:
                question_str = question_str.replace(dict_item, '####')
                var_list.append(dict_item)
        for var in var_list:
            entity_list.append(rdfPrepare.rdf_query_name(var,type,graph))
        return entity_list

    @classmethod
    def var_dict_list(cls, graph):
        var_list = rdfPrepare.rdf_query_allvarient(graph)
        return var_list


    @classmethod
    def room_dict_match(cls, question_str, var_list, graph):
        """
        字典匹配的方式抽取馆室实体,先查询图找到异名列表，匹配异名
        :param question_str:
        :param graph:
        :return:返回正名
        """
        entity_list = []
        entity_list = cls.dict_match(question_str, var_list, "room" , graph)
        return entity_list

    @classmethod
    def resource_dict_match(cls, question_str,var_list, graph):
        """
        字典匹配的方式抽取资源实体,先查询图找到异名列表，匹配异名
        :param question_str:
        :param graph:
        :return:返回正名
        """
        entity_list = []
        entity_list = cls.dict_match(question_str, var_list, "resource", graph)
        return entity_list


    @classmethod
    def floor_dict_match(cls, question_str,var_list, graph):
        """
        字典匹配的方式抽取louceng实体,先查询图找到异名列表，匹配异名
        :param question_str:
        :param graph:
        :return:返回正名
        """
        entity_list = []
        dict_list = rdfPrepare.rdf_query_varientnames('floor',graph)
        for entity in dict_list.keys():
            entity_list += dict_list[entity]
        entity_list = cls.dict_match(question_str, var_list, "floor", graph)
        return entity_list



if __name__=="__main__":
    # g = rdfPrepare.load_graph()
    # var_list = DictMatch2.var_dict_list(g)
    # print(DictMatch2.room_dict_match("我想去典藏馆咋走啊？",var_list,g))
    pass