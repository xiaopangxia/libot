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
import time
import datetime
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
            answer = cls.answer_room_time(entity_dict, graph,"today")
        elif task == 'task_room_time_tomorrow':
            answer = cls.answer_room_time(entity_dict, graph,"tomorrow")
        elif task == 'task_room_time_Monday':
            answer = cls.answer_room_time(entity_dict, graph,"Monday")
        elif task == 'task_room_time_Tuesday':
            answer = cls.answer_room_time(entity_dict, graph,"Tuesday")
        elif task == 'task_room_time_Wednesday':
            answer = cls.answer_room_time(entity_dict, graph,"Wednesday")
        elif task == 'task_room_time_Thursday':
            answer = cls.answer_room_time(entity_dict, graph,"Thursday")
        elif task == 'task_room_time_Friday':
            answer = cls.answer_room_time(entity_dict, graph,"Friday")
        elif task == 'task_room_time_Saturday':
            answer = cls.answer_room_time(entity_dict, graph,"Saturday")
        elif task == 'task_room_time_Sunday':
            answer = cls.answer_room_time(entity_dict, graph,"Sunday")
        elif task == 'task_room_time_borrow':
            answer = cls.answer_room_time_borrow(entity_dict, graph,"today")
        elif task == 'task_room_time_borrow_tomorrow':
            answer = cls.answer_room_time_borrow(entity_dict, graph,"tomorrow")
        elif task == 'task_room_time_borrow_Monday':
            answer = cls.answer_room_time_borrow(entity_dict, graph,"Monday")
        elif task == 'task_room_time_borrow_Tuesday':
            answer = cls.answer_room_time_borrow(entity_dict, graph,"Tuesday")
        elif task == 'task_room_time_borrow_Wednesday':
            answer = cls.answer_room_time_borrow(entity_dict, graph,"Wednesday")
        elif task == 'task_room_time_borrow_Thursday':
            answer = cls.answer_room_time_borrow(entity_dict, graph,"Thursday")
        elif task == 'task_room_time_borrow_Friday':
            answer = cls.answer_room_time_borrow(entity_dict, graph,"Friday")
        elif task == 'task_room_time_borrow_Saturday':
            answer = cls.answer_room_time_borrow(entity_dict, graph,"Saturday")
        elif task == 'task_room_time_borrow_Sunday':
            answer = cls.answer_room_time_borrow(entity_dict, graph,"Sunday")
        elif task == 'task_room_time_openday':
            answer = cls.answer_room_time_openday(entity_dict, graph=graph)
        elif task == 'task_room_contact':
            answer = cls.answer_room_contact(entity_dict, graph=graph)
        elif task == 'task_room_pos':
            answer = cls.answer_room_pos(entity_dict, graph,1)
        elif task == 'task_res_time':
            answer = cls.answer_res_time(entity_dict, graph,"today")
        elif task == 'task_res_time_tomorrow':
            answer = cls.answer_res_time(entity_dict, graph,"tomorrow")
        elif task == 'task_res_time_Monday':
            answer = cls.answer_res_time(entity_dict, graph,"Monday")
        elif task == 'task_res_time_Tuesday':
            answer = cls.answer_res_time(entity_dict, graph,"Tuesday")
        elif task == 'task_res_time_Wednesday':
            answer = cls.answer_res_time(entity_dict, graph,"Wednesday")
        elif task == 'task_res_time_Thursday':
            answer = cls.answer_res_time(entity_dict, graph,"Thursday")
        elif task == 'task_res_time_Friday':
            answer = cls.answer_res_time(entity_dict, graph,"Friday")
        elif task == 'task_res_time_Saturday':
            answer = cls.answer_res_time(entity_dict, graph,"Saturday")
        elif task == 'task_res_time_Sunday':
            answer = cls.answer_res_time(entity_dict, graph,"Sunday")
        elif task == 'task_res_time_openday':
            answer = cls.answer_res_time_openday(entity_dict, graph)
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

    @classmethod
    def answer_res_time_openday(cls, entity_dict, graph):
        '''
        资源开放日
        :param entity_dict:
        :param graph:
        :return:
        '''
        res_in_question = entity_dict['res']
        respons_str = ''
        if res_in_question:
            for target_res in res_in_question:
                room=rdfPrepare.rdf_query_relation(target_res, "rel_part_of_room", graph)
                if(len(room)!=0):
                    if(len(rdfPrepare.rdf_query_propertiy(room[0], "pro_open_day", graph))!=0):
                        respons_str += target_res +"开放日是："+rdfPrepare.rdf_query_propertiy(room[0], "pro_open_day", graph)[0]+"。\n"
                elif(len(rdfPrepare.rdf_query_relation(room[0], "rel_part_of_room", graph))!=0):
                    parent_room = rdfPrepare.rdf_query_relation(room[0], "rel_part_of_room", graph)
                    for p_room in parent_room:
                        if(rdfPrepare.rdf_query_propertiy(p_room, "pro_open_day", graph)):
                            respons_str += target_res + '位于' + p_room.split('_')[2] + '，开放日是：' + rdfPrepare.rdf_query_propertiy(p_room, "pro_open_day", graph)[0] + '。\n'
            return respons_str
        else:
            return None

    @classmethod
    def answer_room_time_openday(cls, entity_dict, graph):
        '''
        馆室开放日
        :param entity_dict:
        :param graph:
        :return:
        '''
        room_in_question = entity_dict['room']
        respons_str =''
        if room_in_question:
            for target_room in room_in_question:
                if (len(rdfPrepare.rdf_query_propertiy(target_room, "pro_open_day", graph)) != 0):
                    respons_str += "_".join(target_room.split('_')[0:3]) + "开放日是：" + \
                                   rdfPrepare.rdf_query_propertiy(target_room, "pro_open_day", graph)[0] + "。\n"
                elif (len(rdfPrepare.rdf_query_relation(target_room, "rel_part_of_room", graph)) != 0):
                    parent_room = rdfPrepare.rdf_query_relation(target_room, "rel_part_of_room", graph)
                    for p_room in parent_room:
                        if (rdfPrepare.rdf_query_propertiy(p_room, "pro_open_day", graph)):
                            respons_str += target_room + '位于' + p_room.split('_')[2] + '，开放日是：' + \
                                           rdfPrepare.rdf_query_propertiy(p_room, "pro_open_day", graph)[0] + '。\n'
            return respons_str
        else:
            return None

    @classmethod
    def answer_room_time(cls, entity_dict, graph,day):
        '''
        馆室开放时间
        '''
        room_in_question = entity_dict['room']
        respons_str=""
        if day=="today":
            respons_str = '今天是' + GraphBaseConfig['now_day'] + '，'
            week_str=time.strftime("%w", time.localtime())
            if str(week_str)=='1':
                week_str="pro_Monday_opentime"
                respons_str =respons_str.replace('星期1', '星期一')
            elif str(week_str)=='2':
                week_str="pro_Tuesday_opentime"
                respons_str = respons_str.replace('星期2', '星期二')
            elif str(week_str)=='3':
                week_str="pro_Wednesday_opentime"
                respons_str = respons_str.replace('星期3', '星期三')
            elif str(week_str)=='4':
                week_str="pro_Thursday_opentime"
                respons_str = respons_str.replace('星期4', '星期四')
            elif str(week_str)=='5':
                week_str="pro_Friday_opentime"
                respons_str = respons_str.replace('星期5', '星期五')
            elif str(week_str)=='6':
                week_str="pro_Saturday_opentime"
                respons_str = respons_str.replace('星期6', '星期六')
            elif str(week_str)=='日':
                week_str="pro_Sunday_opentime"
        elif day=="tomorrow":
            respons_str = '明天是' + GraphBaseConfig['now_day'] + '，'
            week_str = time.strftime("%w", time.localtime())
            if str(week_str) == '1':
                week_str = "pro_Tuesday_opentime"
                respons_str = respons_str.replace('星期1', '星期二')
            elif str(week_str) == '2':
                week_str = "pro_Wednesday_opentime"
                respons_str = respons_str.replace('星期2', '星期三')
            elif str(week_str) == '3':
                week_str = "pro_Thursday_opentime"
                respons_str = respons_str.replace('星期3', '星期四')
            elif str(week_str) == '4':
                week_str = "pro_Friday_opentime"
                respons_str = respons_str.replace('星期4', '星期五')
            elif str(week_str) == '5':
                week_str = "pro_Saturday_opentime"
                respons_str = respons_str.replace('星期5', '星期六')
            elif str(week_str) == '6':
                week_str = "pro_Sunday_opentime"
                respons_str = respons_str.replace('星期6', '星期日')
            elif str(week_str) == '日':
                week_str = "pro_Monday_opentime"
                respons_str = respons_str.replace('星期日', '星期一')
        elif day=="Monday":
            respons_str = '星期一，'
            week_str = "pro_Monday_opentime"
        elif day=="Tuesday":
            respons_str = '星期二，'
            week_str = "pro_Tuesday_opentime"
        elif day=="Wednesday":
            respons_str = '星期三，'
            week_str = "pro_Wednesday_opentime"
        elif day=="Thursday":
            respons_str = '星期四，'
            week_str = "pro_Thursday_opentime"
        elif day=="Friday":
            respons_str = '星期五，'
            week_str = "pro_Friday_opentime"
        elif day == "Saturday":
            respons_str = '星期六，'
            week_str = "pro_Saturday_opentime"
        elif day == "Sunday":
            respons_str = '星期日，'
            week_str = "pro_Sunday_opentime"
        if room_in_question:
            for target_room in room_in_question:
                if(len(rdfPrepare.rdf_query_propertiy(target_room, week_str, graph))!=0):
                    respons_str += "_".join(target_room.split('_')[0:3]) +"开放时间是："+rdfPrepare.rdf_query_propertiy(target_room, week_str, graph)[0]+"。\n"
                elif(len(rdfPrepare.rdf_query_relation(target_room, "rel_part_of_room", graph))!=0):
                    parent_room = rdfPrepare.rdf_query_relation(target_room, "rel_part_of_room", graph)
                    for p_room in parent_room:
                        if(rdfPrepare.rdf_query_propertiy(p_room, week_str, graph)):
                            respons_str += target_room + '位于' + p_room.split('_')[2] + '，开放时间是：' + rdfPrepare.rdf_query_propertiy(p_room, week_str, graph)[0] + '。\n'
            return respons_str
        else:
            return None

    @classmethod
    def answer_room_time_borrow(cls, entity_dict, graph,day):
        '''
        馆室借阅时间
        :param entity_dict:
        :param graph:
        :return:
        '''
        room_in_question = entity_dict['room']
        respons_str = ''
        if day=="today":
            week_str = time.strftime("%w", time.localtime())
            respons_str = '今天是' + GraphBaseConfig['now_day'] + '，'
            if str(week_str)=='1':
                week_str="pro_Monday_borrowtime"
                respons_str =respons_str.replace('星期1', '星期一')
            elif str(week_str)=='2':
                week_str="pro_Tuesday_borrowtime"
                respons_str = respons_str.replace('星期2', '星期二')
            elif str(week_str)=='3':
                week_str="pro_Wednesday_borrowtime"
                respons_str = respons_str.replace('星期3', '星期三')
            elif str(week_str)=='4':
                week_str="pro_Thursday_borrowtime"
                respons_str = respons_str.replace('星期4', '星期四')
            elif str(week_str)=='5':
                week_str="pro_Friday_borrowtime"
                respons_str = respons_str.replace('星期5', '星期五')
            elif str(week_str)=='6':
                week_str="pro_Saturday_borrowtime"
                respons_str = respons_str.replace('星期6', '星期六')
            elif str(week_str)=='日':
                week_str="pro_Sunday_borrowtime"
        elif day=="tomorrow":
            respons_str = '明天是' + GraphBaseConfig['now_day'] + '，'
            week_str = time.strftime("%w", time.localtime())
            if str(week_str) == '1':
                week_str = "pro_Tuesday_borrowtime"
                respons_str = respons_str.replace('星期1', '星期二')
            elif str(week_str) == '2':
                week_str = "pro_Wednesday_borrowtime"
                respons_str = respons_str.replace('星期2', '星期三')
            elif str(week_str) == '3':
                week_str = "pro_Thursday_borrowtime"
                respons_str = respons_str.replace('星期3', '星期四')
            elif str(week_str) == '4':
                week_str = "pro_Friday_borrowtime"
                respons_str = respons_str.replace('星期4', '星期五')
            elif str(week_str) == '5':
                week_str = "pro_Saturday_borrowtime"
                respons_str = respons_str.replace('星期5', '星期六')
            elif str(week_str) == '6':
                week_str = "pro_Sunday_borrowtime"
                respons_str = respons_str.replace('星期6', '星期日')
            elif str(week_str) == '日':
                week_str = "pro_Monday_borrowtime"
                respons_str = respons_str.replace('星期日', '星期一')
        elif day == "Monday":
            respons_str = '星期一，'
            week_str = "pro_Monday_borrowtime"
        elif day == "Tuesday":
            respons_str = '星期二，'
            week_str = "pro_Tuesday_borrowtime"
        elif day == "Wednesday":
            respons_str = '星期三，'
            week_str = "pro_Wednesday_borrowtime"
        elif day == "Thursday":
            respons_str = '星期四，'
            week_str = "pro_Thursday_borrowtime"
        elif day == "Friday":
            respons_str = '星期五，'
            week_str = "pro_Friday_borrowtime"
        elif day == "Saturday":
            respons_str = '星期六，'
            week_str = "pro_Saturday_borrowtime"
        elif day == "Sunday":
            respons_str = '星期日，'
            week_str = "pro_Sunday_borrowtime"
        if room_in_question:
            for target_room in room_in_question:
                if(len(rdfPrepare.rdf_query_propertiy(target_room, week_str, graph))!=0):
                    respons_str += "_".join(target_room.split('_')[0:3]) +"借阅时间是："+rdfPrepare.rdf_query_propertiy(target_room, week_str, graph)[0]+"。\n"
                elif(len(rdfPrepare.rdf_query_relation(target_room, "rel_part_of_room", graph))!=0):
                    parent_room = rdfPrepare.rdf_query_relation(target_room, "rel_part_of_room", graph)
                    for p_room in parent_room:
                        if(rdfPrepare.rdf_query_propertiy(p_room, week_str, graph)):
                            respons_str += target_room + '位于' + p_room.split('_')[2] + '，借阅时间是：' + rdfPrepare.rdf_query_propertiy(p_room, week_str, graph)[0] + '。\n'
            return respons_str
        else:
            return None

    @classmethod
    def answer_res_time(cls, entity_dict, graph,day):
        '''
        资源开放时间
        :param entity_dict:
        :param graph:
        :return:
        '''
        res_in_question = entity_dict['res']
        respons_str=''
        if day=="today":
            respons_str = '今天是' + GraphBaseConfig['now_day'] + '，'
            week_str = time.strftime("%w", time.localtime())
            if str(week_str) == '1':
                week_str = "pro_Monday_opentime"
                respons_str = respons_str.replace('星期1', '星期一')
            elif str(week_str) == '2':
                week_str = "pro_Tuesday_opentime"
                respons_str = respons_str.replace('星期2', '星期二')
            elif str(week_str) == '3':
                week_str = "pro_Wednesday_opentime"
                respons_str = respons_str.replace('星期3', '星期三')
            elif str(week_str) == '4':
                week_str = "pro_Thursday_opentime"
                respons_str = respons_str.replace('星期4', '星期四')
            elif str(week_str) == '5':
                week_str = "pro_Friday_opentime"
                respons_str = respons_str.replace('星期5', '星期五')
            elif str(week_str) == '6':
                week_str = "pro_Saturday_opentime"
                respons_str = respons_str.replace('星期6', '星期六')
            elif str(week_str) == '日':
                week_str = "pro_Sunday_opentime"
        elif day=="tomorrow":
            respons_str = '明天是' + GraphBaseConfig['now_day'] + '，'
            week_str = time.strftime("%w", time.localtime())
            if str(week_str) == '1':
                week_str = "pro_Tuesday_opentime"
                respons_str = respons_str.replace('星期1', '星期二')
            elif str(week_str) == '2':
                week_str = "pro_Wednesday_opentime"
                respons_str = respons_str.replace('星期2', '星期三')
            elif str(week_str) == '3':
                week_str = "pro_Thursday_opentime"
                respons_str = respons_str.replace('星期3', '星期四')
            elif str(week_str) == '4':
                week_str = "pro_Friday_opentime"
                respons_str = respons_str.replace('星期4', '星期五')
            elif str(week_str) == '5':
                week_str = "pro_Saturday_opentime"
                respons_str = respons_str.replace('星期5', '星期六')
            elif str(week_str) == '6':
                week_str = "pro_Sunday_opentime"
                respons_str = respons_str.replace('星期6', '星期日')
            elif str(week_str) == '日':
                week_str = "pro_Monday_opentime"
                respons_str = respons_str.replace('星期日', '星期一')
        elif day=="Monday":
            respons_str = '星期一，'
            week_str = "pro_Monday_opentime"
        elif day=="Tuesday":
            respons_str = '星期二，'
            week_str = "pro_Tuesday_opentime"
        elif day=="Wednesday":
            respons_str = '星期三，'
            week_str = "pro_Wednesday_opentime"
        elif day=="Thursday":
            respons_str = '星期四，'
            week_str = "pro_Thursday_opentime"
        elif day=="Friday":
            respons_str = '星期五，'
            week_str = "pro_Friday_opentime"
        elif day == "Saturday":
            respons_str = '星期六，'
            week_str = "pro_Saturday_opentime"
        elif day == "Sunday":
            respons_str = '星期日，'
            week_str = "pro_Sunday_opentime"
        if res_in_question:
            for target_res in res_in_question:
                room=rdfPrepare.rdf_query_relation(target_res, "rel_part_of_room", graph)
                if(len(room)!=0):
                    if(len(rdfPrepare.rdf_query_propertiy(room[0], week_str, graph))!=0):
                        print(rdfPrepare.rdf_query_propertiy(room[0], week_str, graph))
                        respons_str += target_res +"开放时间是："+rdfPrepare.rdf_query_propertiy(room[0], week_str, graph)[0]+"。\n"
                elif(len(rdfPrepare.rdf_query_relation(room[0], "rel_part_of_room", graph))!=0):
                    parent_room = rdfPrepare.rdf_query_relation(room[0], "rel_part_of_room", graph)
                    for p_room in parent_room:
                        if(rdfPrepare.rdf_query_propertiy(p_room, week_str, graph)):
                            respons_str += target_res + '位于' + p_room.split('_')[2] + '，开放时间是：' + rdfPrepare.rdf_query_propertiy(p_room, week_str, graph)[0] + '。\n'
            return respons_str
        else:
            return None