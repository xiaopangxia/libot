import os
import sys
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)

from model.config.base_config import GraphBaseConfig
from model.kb_prepare.neo4j_prepare import Neo4jPrepare
import time
import datetime
import matplotlib.pyplot as plt
from skimage import io
import numpy as np

class neo4jBot():
    """
    对应问题模式在知识图谱中查找答案
    目前包括馆室位置，馆室开放日，馆室开放时间，馆室联系方式，资源馆室
    """

    @classmethod
    def task_response(cls, task, entity_dict):
        """
        响应hub指派的回答任务，也就是对graphQA类的问题分intent处理
        :param task:
        :return:
        """
        graph=""
        question_str=""
        answer = "GraphQA 什么也没说！"
        if task == 'task_room_time':
            answer = cls.answer_room_time(entity_dict, "today")
        elif task == 'task_room_time_tomorrow':
            answer = cls.answer_room_time(entity_dict, "tomorrow")
        elif task == 'task_room_time_Monday':
            answer = cls.answer_room_time(entity_dict, "Monday")
        elif task == 'task_room_time_Tuesday':
            answer = cls.answer_room_time(entity_dict, graph, "Tuesday")
        elif task == 'task_room_time_Wednesday':
            answer = cls.answer_room_time(entity_dict, graph, "Wednesday")
        elif task == 'task_room_time_Thursday':
            answer = cls.answer_room_time(entity_dict, graph, "Thursday")
        elif task == 'task_room_time_Friday':
            answer = cls.answer_room_time(entity_dict, graph, "Friday")
        elif task == 'task_room_time_Saturday':
            answer = cls.answer_room_time(entity_dict, graph, "Saturday")
        elif task == 'task_room_time_Sunday':
            answer = cls.answer_room_time(entity_dict, graph, "Sunday")
        elif task == 'task_room_time_borrow':
            answer = cls.answer_room_time_borrow(entity_dict, graph, "today")
        elif task == 'task_room_time_borrow_tomorrow':
            answer = cls.answer_room_time_borrow(entity_dict, graph, "tomorrow")
        elif task == 'task_room_time_borrow_Monday':
            answer = cls.answer_room_time_borrow(entity_dict, graph, "Monday")
        elif task == 'task_room_time_borrow_Tuesday':
            answer = cls.answer_room_time_borrow(entity_dict, graph, "Tuesday")
        elif task == 'task_room_time_borrow_Wednesday':
            answer = cls.answer_room_time_borrow(entity_dict, graph, "Wednesday")
        elif task == 'task_room_time_borrow_Thursday':
            answer = cls.answer_room_time_borrow(entity_dict, graph, "Thursday")
        elif task == 'task_room_time_borrow_Friday':
            answer = cls.answer_room_time_borrow(entity_dict, graph, "Friday")
        elif task == 'task_room_time_borrow_Saturday':
            answer = cls.answer_room_time_borrow(entity_dict, graph, "Saturday")
        elif task == 'task_room_time_borrow_Sunday':
            answer = cls.answer_room_time_borrow(entity_dict, graph, "Sunday")
        elif task == 'task_room_time_openday':
            answer = cls.answer_room_time_openday(entity_dict, graph=graph)
        elif task == 'task_room_contact':
            answer = cls.answer_room_contact(entity_dict, graph=graph)
        elif task == 'task_room_pos':
            answer = cls.answer_room_pos(entity_dict)
        elif task == 'task_res_time':
            answer = cls.answer_res_time(entity_dict, graph, "today")
        elif task == 'task_res_time_tomorrow':
            answer = cls.answer_res_time(entity_dict, graph, "tomorrow")
        elif task == 'task_res_time_Monday':
            answer = cls.answer_res_time(entity_dict, graph, "Monday")
        elif task == 'task_res_time_Tuesday':
            answer = cls.answer_res_time(entity_dict, graph, "Tuesday")
        elif task == 'task_res_time_Wednesday':
            answer = cls.answer_res_time(entity_dict, graph, "Wednesday")
        elif task == 'task_res_time_Thursday':
            answer = cls.answer_res_time(entity_dict, graph, "Thursday")
        elif task == 'task_res_time_Friday':
            answer = cls.answer_res_time(entity_dict, graph, "Friday")
        elif task == 'task_res_time_Saturday':
            answer = cls.answer_res_time(entity_dict, graph, "Saturday")
        elif task == 'task_res_time_Sunday':
            answer = cls.answer_res_time(entity_dict, graph, "Sunday")
        elif task == 'task_res_time_openday':
            answer = cls.answer_res_time_openday(entity_dict, graph)
        elif task == 'task_res_pos':
            answer = cls.answer_res_pos(entity_dict, graph, 1)
        elif task == 'task_res_room':
            answer = cls.answer_res_room(entity_dict, graph)
        # 包含类
        elif task == 'task_room_room_l':
            answer = cls.answer_room_room_l(cls=cls, entity_dict=entity_dict, question_str=question_str, graph=graph)
        elif task == 'task_room_room_h':
            answer = cls.answer_room_room_h(cls=cls, entity_dict=entity_dict, question_str=question_str, graph=graph)
        elif task == 'task_room_floor_l':
            answer = cls.answer_room_floor_l(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_room_floor_h':
            answer = cls.answer_room_floor_h(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_res_floor_l':
            answer = cls.answer_res_floor_l(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_res_floor_h':
            answer = cls.answer_res_floor_h(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_res_room_l':
            answer = cls.answer_res_room_l(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_res_room_h':
            answer = cls.answer_res_room_h(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_room_room_a':
            answer = cls.answer_room_room_a(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_floor_room_a':
            answer = cls.answer_floor_room_a(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_room_res_a':
            answer = cls.answer_have_res_a(entity_dict)
        elif task == 'task_floor_res_a':
            answer = cls.answer_have_res_a(entity_dict)
        elif task == 'task_room_room_or_res_a':
            answer = cls.answer_room_room_or_res_a(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_count_res':
            answer = cls.answer_count_res(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_count_floor':
            answer = cls.answer_count_floor(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_floor_count_room':
            answer = cls.answer_floor_count_room(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_res_res_h':
            answer = cls.answer_res_res_h(cls=cls, entity_dict=entity_dict, question_str=question_str, graph=graph)
        elif task == 'task_res_res_a':
            answer = cls.answer_res_res_a(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_room_count_room':
            answer = cls.answer_room_count_room(cls=cls, entity_dict=entity_dict, question_str=question_str,
                                                graph=graph)
        return answer

    @classmethod
    def answer_have_res_a(cls, entity):
        response = ""
        e=""
        if entity['room']:
            e=entity['room'][0]


        elif entity['floor']:
            e=entity['floor'][0]

        ans = Neo4jPrepare.get_reverse_relation_mul(e,'资源')
        if len(ans)==0:
            return "未找到资源\n"
        response += e + "具有如下资源：\n"

        for i in ans:
            #print(i)
            response += i['office_name']+"\n"

        return response










