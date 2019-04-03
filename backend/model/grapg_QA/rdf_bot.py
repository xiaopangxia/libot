# -*- coding: utf-8 -*-
# File: rdf_bot.py
# Author: Liu liting <nkliuliting826@mail.nankai.edu.cn>
# CreateDate: 19-03-31
import os
import sys
# 模块路径引用统一回退到Libbot目录下
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)

from model.config.base_config import GraphBaseConfig
from model.kb_prepare.rdf_prepare import rdfPrepare

class rdfBot():
    """
    对应问题模式在知识图谱中查找答案
    目前包括馆室位置，馆室开放日，馆室开放时间，馆室联系方式，资源馆室
    """
    @classmethod
    def task_response(cls, task, entity_dict, graph):
        """
        响应hub指派的回答任务，也就是对graphQA类的问题分intent处理
        :param task:
        :return:
        """
        answer = "GraphQA 什么也没说！"
        if task == 'task_room_time':
            answer = cls.answer_room_time(entity_dict, graph)
        elif task == 'task_room_contact':
            answer = cls.answer_room_contact(entity_dict, graph=graph)
        elif task == 'task_room_pos':
            answer = cls.answer_room_pos(entity_dict, graph,1)
        elif task == 'task_res_time':
            answer = cls.answer_res_time(entity_dict, graph)
        elif task == 'task_res_pos':
            answer = cls.answer_res_pos(entity_dict, graph,1)
        elif task == 'task_res_room':
            answer = cls.answer_res_room(entity_dict, graph)

        return answer

    @classmethod
    def answer_room_contact(cls, entity_dict, graph):
        if len(entity_dict['room'])!= 0:
            respons_str = ''
            for i in range(len(entity_dict['room'])):
                room_in_question = entity_dict['room'][i]
                if room_in_question:
                    for target_room in room_in_question:
                        if(len(rdfPrepare.rdf_query_propertiy(target_room, "pro_contact_phone", graph))!=0):
                            respons_str += "_".join(target_room.split('_')[0:3]) +"的电话："+rdfPrepare.rdf_query_propertiy(target_room, "pro_contact_phone", graph)[0]+"。\n"
                        elif(len(rdfPrepare.rdf_query_relation(target_room, "rel_part_of_room", graph))!=0):
                            parent_room = rdfPrepare.rdf_query_relation(target_room, "rel_part_of_room", graph)
                            for p_room in parent_room:
                                if(rdfPrepare.rdf_query_propertiy(p_room, "pro_contact_phone", graph)):
                                    respons_str += target_room + '位于' + p_room.split('_')[2] + '，可致电' + p_room.split('_')[2]+"：" + rdfPrepare.rdf_query_propertiy(p_room, "pro_contact_phone", graph)[0] + '。\n'
            return respons_str
        else:
            return None

    @classmethod
    def answer_room_pos(cls, entity_dict, graph, tag):
        if tag:
            respons_str = '您当前位置是' + GraphBaseConfig['now_floor'] + '。\n'
        else:
            respons_str = ''
        if len(entity_dict['room'])!=0:
            for i in range(len(entity_dict['room'])):
                room_in_question = entity_dict['room'][i]
                if room_in_question:
                    for target_room in room_in_question:
                        respons_str += "_".join(target_room.split('_')[0:3])+"位于："
                        if(len(rdfPrepare.rdf_query_relation(target_room, "rel_part_of_floor", graph))!=0):
                            respons_str += rdfPrepare.rdf_query_relation(target_room, "rel_part_of_floor", graph)[0]+','
                        if(len(rdfPrepare.rdf_query_propertiy(target_room, "pro_position_describe", graph))!=0):
                            respons_str += "位置在" + rdfPrepare.rdf_query_propertiy(target_room, "pro_position_describe", graph)[0]
                        respons_str += '。\n'
            return respons_str
        else:
            return None

    @classmethod
    def answer_res_pos(cls, entity_dict, graph, tag):
        if tag:
            respons_str = '您当前位置是' + GraphBaseConfig['now_floor'] + '。\n'
        else:
            respons_str = ''
        if len(entity_dict['res'])!=0:
            for i in range(len(entity_dict['res'])):
                res_in_question = entity_dict['res'][i]
                if res_in_question:
                    for target_res in res_in_question:
                        respons_str += target_res
                        if (len(rdfPrepare.rdf_query_relation(target_res, "rel_part_of_source", graph)) != 0):
                            respons_str += "属于" + rdfPrepare.rdf_query_relation(target_res, "rel_part_of_source", graph)[0]+'。\n'
                        if (len(rdfPrepare.rdf_query_relation(target_res, "rel_part_of_room", graph)) != 0):
                            res_part_room = rdfPrepare.rdf_query_relation(target_res, "rel_part_of_room", graph)[0]
                            respons_str += '存于' + res_part_room+'。\n'
                            dict_list = {'room': [[res_part_room]]}
                            new_answer = cls.answer_room_pos(dict_list,graph,0)
                            if new_answer is not None:
                                respons_str += new_answer
            return respons_str
        else:
            return None

    @classmethod
    def answer_res_room(cls, entity_dict, graph):
        respons_str = ''
        if len(entity_dict['res'])!=0:
            for i in range(len(entity_dict['res'])):
                res_in_question = entity_dict['res'][i]
                if res_in_question:
                    for target_res in res_in_question:
                        if (len(rdfPrepare.rdf_query_relation(target_res, "rel_part_of_source", graph)) != 0):
                            respons_str += "属于" + rdfPrepare.rdf_query_relation(target_res, "rel_part_of_source", graph)[0]+'。\n'
                        if (len(rdfPrepare.rdf_query_relation(target_res, "rel_part_of_room", graph)) != 0):
                            res_part_room = rdfPrepare.rdf_query_relation(target_res, "rel_part_of_room", graph)[0]
                            respons_str += '存于' + res_part_room+'。\n'
                        else:
                            respons_str += '呀，我不知道了！'
            return respons_str
        else:
            return None







