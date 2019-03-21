# -*- coding: utf-8 -*-
# File: json_bot.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-10
import os
import sys
# 模块路径引用统一回退到Libbot目录下
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)


from model.kb_prepare.json_prepare import jsonPrepare
import Levenshtein
from model.config.base_config import GraphBaseConfig
class jsonBot():
    """
    用有限的json格式数据处理graphQA的问题
    目前包括馆室位置，馆室开放日，馆室开放时间，馆室联系方式，资源馆室
    """
    @classmethod
    def task_response(cls, task, question_str, entity_dict):
        """
        响应hub指派的回答任务，也就是对graphQA类的问题分intent处理
        :param task:
        :return:
        """
        answer = "GraphQA 什么也没说！"
        if task == 'task_room_time':
            answer = cls.answer_room_time(question_str, entity_dict)
        elif task == 'task_room_contact':
            answer = cls.answer_room_contact(question_str, entity_dict)
        elif task == 'task_room_pos':
            answer = cls.answer_room_pos(question_str, entity_dict)
        elif task == 'task_res_time':
            answer = cls.answer_res_time(question_str, entity_dict)
        elif task == 'task_res_pos':
            answer = cls.answer_res_pos(question_str, entity_dict)
        elif task == 'task_res_room':
            answer = cls.answer_res_room(question_str, entity_dict)

        return answer


    @classmethod
    def answer_room_time(cls, question_str, entity_dict):
        room_in_question = entity_dict['room']
        room_list = jsonPrepare.load_room_json()
        respons_str = '今天是' + GraphBaseConfig['now_day']+'。'
        have_answer = 0
        for target_room in room_in_question:
            for room in room_list:
                if target_room in room['title']:
                    if room['open_time'] != '':
                        respons_str += room['title']+'开放时间'+room['open_time']+'。'
                        have_answer = 1
                    elif room['open_date'] != '':
                        respons_str += room['title']+'开放日'+room['open_date']+'。'
                        have_answer = 1
        if have_answer == 1:
            return respons_str
        else:
            return None

    @classmethod
    def answer_room_contact(cls, question_str, entity_dict):
        room_in_question = entity_dict['room']
        room_list = jsonPrepare.load_room_json()
        respons_str = ''
        have_answer = 0
        for target_room in room_in_question:
            for room in room_list:
                if target_room in room['title']:
                    if room['contact'] != '':
                        have_answer = 1
                        respons_str += room['title']+'联系方式'+room['contact']+'。'
                    elif room['part_of'] != '':
                        parent_room = room['part_of']
                        for p_room in room_list:
                            if parent_room == p_room['title'] and p_room['contact'] != '':
                                respons_str += room['title'] + '位于' + parent_room + '可以联系'+parent_room + '联系方式' + room['contact'] + '。'
        if have_answer == 1:
            return respons_str
        else:
            return None


    @classmethod
    def answer_room_pos(cls, question_str, entity_dict):
        room_in_question = entity_dict['room']
        room_list = jsonPrepare.load_room_json()
        respons_str = '您当前位置是' + GraphBaseConfig['now_floor'] + '。'
        have_answer = 0
        for target_room in room_in_question:
            for room in room_list:
                if target_room in room['title']:
                    respons_str += (room['title']+'位于')
                    if room['part_of'] != '':
                        respons_str += room['part_of']
                        have_answer = 1
                    if room['floor'] != '':
                        respons_str += room['floor']
                        have_answer = 1
                    if room['position'] != '':
                        respons_str += '位置在'+room['position']
                        have_answer = 1
                    respons_str += '。'

        if have_answer == 1:
            return respons_str
        else:
            return None

    @classmethod
    def answer_res_time(cls, question_str, entity_dict):
        res_in_question = entity_dict['res']
        res_list = jsonPrepare.load_res_json()
        respons_str = ''
        have_answer = 0
        for target_res in res_in_question:
            for res in res_list:
                if target_res in res['title']:
                    respons_str += res['title']
                    if res['part_of'] != '':
                        respons_str += '属于' + res['part_of']
                    if res['res_room'] != '':
                        respons_str += '存于' + res['res_room']+'。'
                        new_answer = cls.answer_room_time(res['res_room']+'什么时候开？', {'room':[res['res_room']]})
                        if new_answer is not None:
                            respons_str += new_answer
                            have_answer = 1

        if have_answer == 1:
            return respons_str
        else:
            return None

    @classmethod
    def answer_res_pos(cls, question_str, entity_dict):
        res_in_question = entity_dict['res']
        res_list = jsonPrepare.load_res_json()
        respons_str = ''
        have_answer = 0
        for target_res in res_in_question:
            for res in res_list:
                if Levenshtein.distance(target_res, res['title']) <= len(target_res) / 5 or target_res in res['title']:
                    respons_str += res['title']
                    if res['part_of'] != '':
                        respons_str += '属于' + res['part_of']
                    if res['res_room'] != '':
                        respons_str += '存于' + res['res_room'] + '。'
                        new_answer = cls.answer_room_pos(res['res_room'] + '在哪里？', {'room': [res['res_room']]})
                        if new_answer is not None:
                            respons_str += new_answer
                            have_answer = 1
        if have_answer == 1:
            return respons_str
        else:
            return None

    @classmethod
    def answer_res_room(cls, question_str, entity_dict):
        res_in_question = entity_dict['res']
        res_list = jsonPrepare.load_res_json()
        respons_str = ''
        for target_res in res_in_question:
            for res in res_list:
                if Levenshtein.distance(target_res, res['title']) <= len(target_res)/5 or target_res in res['title']:
                    respons_str += res['title']
                    if res['part_of'] != '':
                        respons_str += '属于'+res['part_of']
                    if res['res_room'] != '':
                        respons_str += '存于'+res['res_room']
                    else:
                        respons_str += '在哪里不好说'
                    respons_str += '。'
        return respons_str


if __name__ == '__main__':
    pass



