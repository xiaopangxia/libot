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
import numpy as np
class rdfBot():
    """
    对应问题模式在知识图谱中查找答案
    目前包括馆室位置，馆室开放日，馆室开放时间，馆室联系方式，资源馆室
    """
    @classmethod
    def task_response(cls, task, entity_dict, question_str, graph):
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
            answer = cls.answer_room_navi(entity_dict, graph,1)
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
        #包含类
        elif task == 'task_room_room_l':
            answer = cls.answer_room_room_l(cls=cls,entity_dict=entity_dict, question_str=question_str,graph=graph)
        elif task == 'task_room_room_h':
            answer = cls.answer_room_room_h(cls=cls,entity_dict=entity_dict, question_str=question_str,graph=graph)
        elif task == 'task_room_floor_l':
            answer = cls.answer_room_floor_l(cls=cls,entity_dict=entity_dict, graph=graph)
        elif task == 'task_room_floor_h':
            answer = cls.answer_room_floor_h(cls=cls,entity_dict=entity_dict, graph=graph)
        elif task == 'task_res_floor_l':
            answer = cls.answer_res_floor_l(cls=cls,entity_dict=entity_dict, graph=graph)
        elif task == 'task_res_floor_h':
            answer = cls.answer_res_floor_h(cls=cls,entity_dict=entity_dict, graph=graph)
        elif task == 'task_res_room_l':
            answer = cls.answer_res_room_l(cls=cls,entity_dict=entity_dict, graph=graph)
        elif task == 'task_res_room_h':
            answer = cls.answer_res_room_h(cls=cls,entity_dict=entity_dict, graph=graph)
        elif task == 'task_room_room_a':
            answer = cls.answer_room_room_a(cls=cls,entity_dict=entity_dict, graph=graph)
        elif task == 'task_floor_room_a':
            answer = cls.answer_floor_room_a(cls=cls,entity_dict=entity_dict, graph=graph)
        elif task == 'task_room_res_a':
            answer = cls.answer_room_res_a(cls=cls,entity_dict=entity_dict, graph=graph)
        elif task == 'task_floor_res_a':
            answer = cls.answer_floor_res_a(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_room_room_or_res_a':
            answer = cls.answer_room_room_or_res_a(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_count_res':
            answer = cls.answer_count_res(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_count_floor':
            answer = cls.answer_count_floor(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_floor_count_room':
            answer = cls.answer_floor_count_room(cls=cls, entity_dict=entity_dict, graph=graph)
        elif task == 'task_res_res_h':
            answer = cls.answer_res_res_h(cls=cls, entity_dict=entity_dict, question_str=question_str,graph=graph)
        elif task == 'task_res_res_a':
            answer = cls.answer_res_res_a(cls=cls, entity_dict=entity_dict,graph=graph)
        elif task == 'task_room_count_room':
            answer = cls.answer_room_count_room(cls=cls, entity_dict=entity_dict, question_str=question_str,graph=graph)


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
    def answer_room_navi(cls, entity_dict, graph, tag):
        if tag:
            respons_str = '\n您当前位置是' + GraphBaseConfig['now_floor'] + '。\n'
        else:
            respons_str = ''
        machine = GraphBaseConfig['now_machine']
        #print(machine)
        destination = entity_dict['room'][0]

        des_room = rdfPrepare.rdf_query_relation(destination[0], 'rel_part_of_room', graph)
        #print(des_room)
        if len(des_room)<=0:
            respons_str += destination[0]
            if len(destination)>1:
                for d in destination[1:]:
                    respons_str += '和' + d
            respons_str += "不在该馆区。\n"
            return respons_str

        #print(len(entity_dict),type(entity_dict),entity_dict)

        des_room = des_room[0]
        #print(des_room)
        machine_room = rdfPrepare.rdf_query_relation(machine, 'rel_part_of_room', graph)[0]
        machine_floor = rdfPrepare.rdf_query_relation(machine, 'rel_part_of_floor', graph)[0]
        father_room = rdfPrepare.rdf_query_relation(des_room, 'rel_part_of_room', graph)
        if len(destination)>1:
            for jud in destination:
                if jud.find(machine_room) == -1:
                    #print(jud,destination,machine_room)
                    del jud
                    #print(destination)
        if len(father_room)>0:
            father_room = father_room[0]
        ##print('father',father_room)
        des_floor = []
        form_des = ''
        if destination[0].find('_') == -1:
            #respons_str += (destination[0])
            form_des = destination[0]
        else:
            arr = destination[0].split('_')
            if len(arr) == 3:
                #respons_str += (arr[len(arr) - 1])
                form_des = arr[len(arr) - 1]
            else:
                #respons_str += (arr[len(arr) - 2])
                form_des = arr[len(arr) - 2]
        for des in destination:
            des_floor.append(rdfPrepare.rdf_query_relation(des, 'rel_part_of_floor', graph)[0])
        #print(machine_room,machine_floor,des_room,des_floor)
        #if False and machine_floor in des_floor:
        if machine_floor in des_floor:

            pos_near_machine = rdfPrepare.rdf_query_navi_propertiy(machine,'pro_neighbor',graph)
            near_machine_dir = rdfPrepare.rdf_query_navi_propertiy(machine,'pro_neighbor_dir',graph)
            near_machine_dis = rdfPrepare.rdf_query_navi_propertiy_dis(machine,'pro_nei_dis',graph)

            near_des = rdfPrepare.rdf_query_navi_propertiy(machine,'pro_destination',graph)
            near_des_dir = rdfPrepare.rdf_query_navi_propertiy(machine, 'pro_destination_dir', graph)
            near_des_dis = rdfPrepare.rdf_query_navi_propertiy_dis(machine, 'pro_des_dis', graph)
            #print(pos_near_machine, near_machine_dir, near_machine_dis)
            #print(pos_near_machine,near_machine_dir,near_machine_dis,near_des,near_des_dir,near_des_dis)
            candidate_des=[]
            #print(destination,near_des)
            for des_3 in destination:
                if des_3 in near_des:
                    candidate_des.append(des_3)
            #print(candidate_des,near_des,destination,"not straight")
            if len(candidate_des)>0:
                #print(candidate_des,near_des)
                #print("yes")
                distance = 10000000
                final_des = ''
                for i in range(len(near_des)):
                    #print(near_des,candidate_des)
                    if near_des[i] in candidate_des and distance>int(near_des_dis[i]):
                        distance = int(near_des_dis[i])
                        final_des = near_des[i]
                        final_dir = near_des_dir[i]
                #print(distance.split('m')[0])
                if distance<100:
                    respons_str += form_des+'在您'+final_dir+"面"+str(distance)+"米处。\n"

                else:
                    respons_str += '向'+final_dir+"走"+str(distance)+"米您就能找到"+form_des+"。\n"
            else:
                f_distance = 10000000
                final_des = ''
                final_dir = ''
                flag = True
                conors = pos_near_machine
                while(flag):
                    #print("while")
                    for conorindex in range(len(conors)):
                        tmpdistance = 10000000
                        conor = conors[conorindex]
                        flag = False
                        #f_distance = near_machine_dis[conorindex]
                        #pos_near_conor = rdfPrepare.rdf_query_navi_propertiy(conor, 'pro_neighbor', graph)
                        #near_conor_dir = rdfPrepare.rdf_query_navi_propertiy(conor, 'pro_neighbor_dir', graph)
                        #near_conor_dis = rdfPrepare.rdf_query_navi_propertiy_dis(conor, 'pro_nei_dis', graph)
                        conor_des = rdfPrepare.rdf_query_navi_propertiy(conor, 'pro_destination', graph)
                        conor_des_dir = rdfPrepare.rdf_query_navi_propertiy(conor, 'pro_destination_dir', graph)
                        conor_des_dis = rdfPrepare.rdf_query_navi_propertiy_dis(conor, 'pro_des_dis', graph)
                        #print(conor_des,conor_des_dir,conor_des_dis)
                        for des_4 in destination:
                            if des_4 in conor_des:
                                candidate_des.append(des_4)
                        #print(candidate_des)
                        if len(candidate_des) > 0:
                            flag = False
                            for i in range(len(conor_des)):
                                # print(near_des,candidate_des)
                                tmpdistance = int(near_machine_dis[conorindex])+int(conor_des_dis[i])
                                if conor_des[i] in candidate_des and f_distance > tmpdistance:
                                    f_distance = tmpdistance
                                    final_conor = conorindex
                                    final_dir = conor_des_dir[i]
                                    f_dis = conor_des_dis[i]
                            # print(distance.split('m')[0])
                    respons_str += '先向' + near_machine_dir[final_conor]+"走"+str(near_machine_dis[final_conor])+'米直到一个拐角，'
                    if int(f_dis) < 100:
                        respons_str += form_des + '在您' + final_dir + "面" + str(f_dis) + "米处。\n"

                    else:
                        #print("else")
                        respons_str += '再向' + final_dir + "走" + str(f_dis) + "米您就能找到" + form_des + "。\n"
                #print(respons_str,"llll")

            #respons_str += 'same floor.\n'
        elif machine_room == des_room:
            respons_str += form_des
            first = des_floor[0]
            if first.find(des_room)!=-1:
                respons_str += '在本馆区'+first.split('_')[1]+'层'
            if len(des_floor)>1:
                for sub_floor in des_floor[1:]:
                    if sub_floor.find(des_room) == -1:
                        continue
                    print(sub_floor)
                    respons_str += '和'+sub_floor.split('_')[1]+"层"
            respons_str += '。\n'
        elif (machine_room == father_room):
            respons_str += form_des
            r = des_room

            if r.find('_') == -1:
                respons_str += '在本馆区的' + (r) + '。\n位于'
                first = des_floor[0]

                respons_str += '本馆区的' + first.split('_')[1] + '层'
                if len(des_floor) > 1:
                    for sub_floor in des_floor[1:]:
                        respons_str += '、' + sub_floor.split('_')[1] + "层"
                respons_str += '。\n'
            else:
                arr = r.split('_')
                #print(arr)
                if len(arr) == 3:
                    respons_str += '在本馆区的' + (arr[len(arr) - 1]) + '。\n位于'
                else:
                    #print(arr)
                    respons_str += '在本馆区的' + (arr[len(arr) - 2]) + '。\n位于'
                first = des_floor[0]

                respons_str += '本馆区的' + first.split('_')[1] + '层'
                if len(des_floor) > 1:
                    for sub_floor in des_floor[1:]:
                        respons_str += '、' + sub_floor.split('_')[1] + "层"
                respons_str += '。\n'

        else:
            respons_str += form_des
            r = des_room

            if r.find('_') == -1:
                respons_str += '不在该馆区。'+form_des+'在'+(r)+'。\n'
            else:
                arr = r.split('_')
                print(arr)
                if len(arr) == 3:
                    respons_str += '不在该馆区。'+form_des+'在'+(arr[len(arr) - 1])+'。\n'
                else:
                    print(arr)
                    respons_str += '不在该馆区。'+form_des+'在'+(arr[len(arr) - 2])+'。\n'
        return respons_str

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
        if len(entity_dict['res'])!= 0:
            respons_str = ''
            for i in range(len(entity_dict['res'])):
                res_in_question = entity_dict['res'][i]
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
        if len(entity_dict['room'])!= 0:
            respons_str = ''
            for i in range(len(entity_dict['room'])):
                room_in_question = entity_dict['room'][i]
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
        馆室开放时间（当天、明天、星期）
        '''
        if len(entity_dict['room'])!= 0:
            respons_str = ''
            flag_respons_str=''
            for i in range(len(entity_dict['room'])):
                room_in_question = entity_dict['room'][i]
                if room_in_question:
                    if day=="today":
                        respons_str ="今天是"
                        week_str=time.strftime("%w", time.localtime())
                        if str(week_str)=='1':
                            week_str="pro_Monday_opentime"
                            respons_str =respons_str+ '星期一，'
                        elif str(week_str)=='2':
                            week_str="pro_Tuesday_opentime"
                            respons_str = respons_str+'星期二，'
                        elif str(week_str)=='3':
                            week_str="pro_Wednesday_opentime"
                            respons_str = respons_str+'星期三，'
                        elif str(week_str)=='4':
                            week_str="pro_Thursday_opentime"
                            respons_str = respons_str+'星期四,'
                        elif str(week_str)=='5':
                            week_str="pro_Friday_opentime"
                            respons_str = respons_str+'星期五,'
                        elif str(week_str)=='6':
                            week_str="pro_Saturday_opentime"
                            respons_str = respons_str+'星期六,'
                        elif str(week_str)=='日':
                            week_str="pro_Sunday_opentime"
                            respons_str = respons_str+'星期天,'
                    elif day=="tomorrow":
                        respons_str = '明天是'
                        week_str = time.strftime("%w", time.localtime())
                        if str(week_str) == '1':
                            week_str = "pro_Tuesday_opentime"
                            respons_str =respons_str+'星期二,'
                        elif str(week_str) == '2':
                            week_str = "pro_Wednesday_opentime"
                            respons_str = respons_str+'星期三,'
                        elif str(week_str) == '3':
                            week_str = "pro_Thursday_opentime"
                            respons_str = respons_str+'星期四,'
                        elif str(week_str) == '4':
                            week_str = "pro_Friday_opentime"
                            respons_str = respons_str+'星期五,'
                        elif str(week_str) == '5':
                            week_str = "pro_Saturday_opentime"
                            respons_str = respons_str+ '星期六,'
                        elif str(week_str) == '6':
                            week_str = "pro_Sunday_opentime"
                            respons_str = respons_str+'星期日,'
                        elif str(week_str) == '日':
                            week_str = "pro_Monday_opentime"
                            respons_str = respons_str+'星期一,'
                    elif day=="Monday":
                        respons_str = '星期一'
                        week_str = "pro_Monday_opentime"
                    elif day=="Tuesday":
                        respons_str = '星期二'
                        week_str = "pro_Tuesday_opentime"
                    elif day=="Wednesday":
                        respons_str = '星期三'
                        week_str = "pro_Wednesday_opentime"
                    elif day=="Thursday":
                        respons_str = '星期四'
                        week_str = "pro_Thursday_opentime"
                    elif day=="Friday":
                        respons_str = '星期五'
                        week_str = "pro_Friday_opentime"
                    elif day == "Saturday":
                        respons_str = '星期六'
                        week_str = "pro_Saturday_opentime"
                    elif day == "Sunday":
                        respons_str = '星期日'
                        week_str = "pro_Sunday_opentime"
                    flag_respons_str=respons_str
                    if room_in_question:
                        for target_room in room_in_question:
                            if(len(rdfPrepare.rdf_query_propertiy(target_room, week_str, graph))!=0):
                                respons_str += "_".join(target_room.split('_')[0:3]) +"开放时间是："+rdfPrepare.rdf_query_propertiy(target_room, week_str, graph)[0]+"。\n"
                            elif(len(rdfPrepare.rdf_query_relation(target_room, "rel_part_of_room", graph))!=0):
                                parent_room = rdfPrepare.rdf_query_relation(target_room, "rel_part_of_room", graph)
                                for p_room in parent_room:
                                    if(rdfPrepare.rdf_query_propertiy(p_room, week_str, graph)):
                                        respons_str +=  '开放时间是：' + rdfPrepare.rdf_query_propertiy(p_room, week_str, graph)[0] +','+ target_room + '位于' + p_room.split('_')[2] +'。\n'
            if(respons_str==flag_respons_str):
                return "该馆室当天不开放。"
            else:
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
        if len(entity_dict['room'])!= 0:
            respons_str = ''
            flag_respons_str=''
            for i in range(len(entity_dict['room'])):
                room_in_question = entity_dict['room'][i]
                if day=="today":
                    week_str = time.strftime("%w", time.localtime())
                    respons_str = '今天是'
                    if str(week_str)=='1':
                        week_str="pro_Monday_borrowtime"
                        respons_str =respons_str+'星期一，'
                    elif str(week_str)=='2':
                        week_str="pro_Tuesday_borrowtime"
                        respons_str = respons_str+ '星期二，'
                    elif str(week_str)=='3':
                        week_str="pro_Wednesday_borrowtime"
                        respons_str = respons_str+'星期三，'
                    elif str(week_str)=='4':
                        week_str="pro_Thursday_borrowtime"
                        respons_str = respons_str+ '星期四，'
                    elif str(week_str)=='5':
                        week_str="pro_Friday_borrowtime"
                        respons_str = respons_str+'星期五，'
                    elif str(week_str)=='6':
                        week_str="pro_Saturday_borrowtime"
                        respons_str = respons_str+'星期六，'
                    elif str(week_str)=='日':
                        week_str="pro_Sunday_borrowtime"
                        respons_str = respons_str + '星期日，'
                elif day == "tomorrow":
                    respons_str = '明天是'
                    week_str = time.strftime("%w", time.localtime())
                    if str(week_str) == '1':
                        week_str = "pro_Tuesday_borrowtime"
                        respons_str = respons_str + '星期二,'
                    elif str(week_str) == '2':
                        week_str = "pro_Wednesday_borrowtime"
                        respons_str = respons_str + '星期三,'
                    elif str(week_str) == '3':
                        week_str = "pro_Thursday_borrowtime"
                        respons_str = respons_str + '星期四,'
                    elif str(week_str) == '4':
                        week_str = "pro_Friday_borrowtime"
                        respons_str = respons_str + '星期五,'
                    elif str(week_str) == '5':
                        week_str = "pro_Saturday_borrowtime"
                        respons_str = respons_str + '星期六,'
                    elif str(week_str) == '6':
                        week_str = "pro_Sunday_borrowtime"
                        respons_str = respons_str + '星期日,'
                    elif str(week_str) == '日':
                        week_str = "pro_Monday_borrowtime"
                        respons_str = respons_str + '星期一,'
                elif day == "Monday":
                    respons_str = '星期一'
                    week_str = "pro_Monday_borrowtime"
                elif day == "Tuesday":
                    respons_str = '星期二'
                    week_str = "pro_Tuesday_borrowtime"
                elif day == "Wednesday":
                    respons_str = '星期三'
                    week_str = "pro_Wednesday_borrowtime"
                elif day == "Thursday":
                    respons_str = '星期四'
                    week_str = "pro_Thursday_borrowtime"
                elif day == "Friday":
                    respons_str = '星期五'
                    week_str = "pro_Friday_borrowtime"
                elif day == "Saturday":
                    respons_str = '星期六'
                    week_str = "pro_Saturday_borrowtime"
                elif day == "Sunday":
                    respons_str = '星期日'
                    week_str = "pro_Sunday_borrowtime"
                flag_respons_str = respons_str
                if room_in_question:
                    for target_room in room_in_question:
                        if(len(rdfPrepare.rdf_query_propertiy(target_room, week_str, graph))!=0):
                            respons_str += "_".join(target_room.split('_')[0:3]) +"借阅时间是："+rdfPrepare.rdf_query_propertiy(target_room, week_str, graph)[0]+"。\n"
                        elif(len(rdfPrepare.rdf_query_relation(target_room, "rel_part_of_room", graph))!=0):
                            parent_room = rdfPrepare.rdf_query_relation(target_room, "rel_part_of_room", graph)
                            for p_room in parent_room:
                                if(rdfPrepare.rdf_query_propertiy(p_room, week_str, graph)):
                                    respons_str += '借阅时间是：' + rdfPrepare.rdf_query_propertiy(p_room, week_str, graph)[0] + ','+target_room + '位于' + p_room.split('_')[2] + '。\n'

            if(respons_str==flag_respons_str):
                return "该馆室当天不可借阅。"
            else:
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
        if len(entity_dict['res'])!= 0:
            respons_str = ''
            flag_respons_str=''
            for i in range(len(entity_dict['res'])):
                res_in_question = entity_dict['res'][i]
                if res_in_question:
                    if day=="today":
                        respons_str ="今天是"
                        week_str=time.strftime("%w", time.localtime())
                        if str(week_str)=='1':
                            week_str="pro_Monday_opentime"
                            respons_str =respons_str+ '星期一，'
                        elif str(week_str)=='2':
                            week_str="pro_Tuesday_opentime"
                            respons_str = respons_str+'星期二，'
                        elif str(week_str)=='3':
                            week_str="pro_Wednesday_opentime"
                            respons_str = respons_str+'星期三，'
                        elif str(week_str)=='4':
                            week_str="pro_Thursday_opentime"
                            respons_str = respons_str+'星期四,'
                        elif str(week_str)=='5':
                            week_str="pro_Friday_opentime"
                            respons_str = respons_str+'星期五,'
                        elif str(week_str)=='6':
                            week_str="pro_Saturday_opentime"
                            respons_str = respons_str+'星期六,'
                        elif str(week_str)=='日':
                            week_str="pro_Sunday_opentime"
                            respons_str = respons_str+'星期天,'
                    elif day=="tomorrow":
                        respons_str = '明天是'
                        week_str = time.strftime("%w", time.localtime())
                        if str(week_str) == '1':
                            week_str = "pro_Tuesday_opentime"
                            respons_str =respons_str+'星期二,'
                        elif str(week_str) == '2':
                            week_str = "pro_Wednesday_opentime"
                            respons_str = respons_str+'星期三,'
                        elif str(week_str) == '3':
                            week_str = "pro_Thursday_opentime"
                            respons_str = respons_str+'星期四,'
                        elif str(week_str) == '4':
                            week_str = "pro_Friday_opentime"
                            respons_str = respons_str+'星期五,'
                        elif str(week_str) == '5':
                            week_str = "pro_Saturday_opentime"
                            respons_str = respons_str+ '星期六,'
                        elif str(week_str) == '6':
                            week_str = "pro_Sunday_opentime"
                            respons_str = respons_str+'星期日,'
                        elif str(week_str) == '日':
                            week_str = "pro_Monday_opentime"
                            respons_str = respons_str+'星期一,'
                    elif day=="Monday":
                        respons_str = '星期一'
                        week_str = "pro_Monday_opentime"
                    elif day=="Tuesday":
                        respons_str = '星期二'
                        week_str = "pro_Tuesday_opentime"
                    elif day=="Wednesday":
                        respons_str = '星期三'
                        week_str = "pro_Wednesday_opentime"
                    elif day=="Thursday":
                        respons_str = '星期四'
                        week_str = "pro_Thursday_opentime"
                    elif day=="Friday":
                        respons_str = '星期五'
                        week_str = "pro_Friday_opentime"
                    elif day == "Saturday":
                        respons_str = '星期六'
                        week_str = "pro_Saturday_opentime"
                    elif day == "Sunday":
                        respons_str = '星期日'
                        week_str = "pro_Sunday_opentime"
                    flag_respons_str=respons_str
                    for target_res in res_in_question:
                        room=rdfPrepare.rdf_query_relation(target_res, "rel_part_of_room", graph)
                        if(len(room)!=0):
                            if(len(rdfPrepare.rdf_query_propertiy(room[0], week_str, graph))!=0):
                                respons_str += target_res +"开放时间是："+rdfPrepare.rdf_query_propertiy(room[0], week_str, graph)[0]+"。\n"
                        elif(len(rdfPrepare.rdf_query_relation(room[0], "rel_part_of_room", graph))!=0):
                            parent_room = rdfPrepare.rdf_query_relation(room[0], "rel_part_of_room", graph)
                            for p_room in parent_room:
                                if(rdfPrepare.rdf_query_propertiy(p_room, week_str, graph)):
                                    respons_str += '开放时间是：' + rdfPrepare.rdf_query_propertiy(p_room, week_str, graph)[0] + ','+target_res + '位于' + p_room.split('_')[2] + '。\n'
            if (respons_str == flag_respons_str):
                return "该资源当天不开放。"
            else:
                return respons_str
        else:
            return None
    #馆室馆室
    def answer_room_room_l(cls,entity_dict,question_str,graph):
        entity_count = 1
        arr = []
        if len(entity_dict['room']) > 0:
            for i in entity_dict['room']:
                if len(i) == 0:
                    continue
                index = question_str.find(i[0])
                if index == -1:
                    index = len(entity_dict['room'])-entity_count
                    entity_count = entity_count+1
                arr.append(index)
            # print(arr)
            arr_index = np.argsort(np.array(arr))
            # print(arr_index)
            entity_dict2 = []
            for i in entity_dict['room']:
                if len(i) == 0:
                    continue
                entity_dict2.append(i)

            for i in range(len(entity_dict['room'])):
                if len(entity_dict['room'][i]) == 0:
                    continue
                # print(arr_index[i],entity_dict2[arr_index[i]])
                entity_dict['room'][i] = entity_dict2[arr_index[i]]
        room_in_question = entity_dict['room']
        #print(room_in_question)
        respons_str = ''

        ans=[]
        father = room_in_question[len(room_in_question) - 1][0]

        count_yes = 0
        count_no = 0
        #print(len(room_in_question[:-1]))
        for target in room_in_question[:-1]:
            if (len(rdfPrepare.rdf_query_relation(target[0], "rel_part_of_room", graph))<=0):
                ans.append(0)
                continue
            if (rdfPrepare.rdf_query_relation(target[0], "rel_part_of_room", graph)[0] == father):
                ans.append(1)
            else :
                ans.append(0)
        #print(ans)

        index = 0
        for target in room_in_question[:-1]:
            if ans[index]:
                if count_yes == 0:
                    count_yes = count_yes + 1
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += (target[0])
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += (arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += (arr[len(arr) - 2])
                    #respons_str += target[0]

                else:
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += ('和' + target[0])
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += ('和' + arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += ('和' + arr[len(arr) - 2])

            index = index + 1
        if count_yes>0:
            respons_str += ('在' + father+"。\n")

        index = 0
        for target in room_in_question[:-1]:
            #print(index)
            if ans[index] == 0:
                if count_no == 0:
                    count_no = count_no+1
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += (target[0])
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += (arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += (arr[len(arr) - 2])

                else:
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += ('和' + target[0])
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += ('和' + arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += ('和' + arr[len(arr) - 2])

            index = index + 1
        if count_no > 0:
            respons_str += ('不在' + father+"。\n")


        return respons_str


    def answer_room_room_h(cls,entity_dict,question_str,graph):
        entity_count = 1
        arr = []
        if len(entity_dict['room']) > 0:
            for i in entity_dict['room']:
                if len(i) == 0:
                    continue
                index = question_str.find(i[0])
                if index == -1:
                    index = len(entity_dict['room'])-entity_count
                    entity_count = entity_count+1
                arr.append(index)
            # print(arr)
            arr_index = np.argsort(np.array(arr))
            # print(arr_index)
            entity_dict2 = []
            for i in entity_dict['room']:
                if len(i) == 0:
                    continue
                entity_dict2.append(i)

            for i in range(len(entity_dict['room'])):
                if len(entity_dict['room'][i]) == 0:
                    continue
                # print(arr_index[i],entity_dict2[arr_index[i]])
                entity_dict['room'][i] = entity_dict2[arr_index[i]]
        room_in_question = entity_dict['room']
        print(room_in_question)
        respons_str = ''

        ans=[]
        father = room_in_question[0][0]
        #print(father)
        count_yes = 0
        count_no = 0
        #print(len(room_in_question[:-1]))
        for target in room_in_question[1:]:
            flag = 0
            if (len(target)) == 0:
                continue
            for t in target:
                if (rdfPrepare.rdf_query_relation(t, "rel_part_of_room", graph)[0] == father):
                    flag = 1
            ans.append(flag)

        #print(ans)

        index = 0
        for target in room_in_question[1:]:
            if ans[index]:
                if count_yes == 0:
                    count_yes = count_yes + 1
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += (father+'有'+target[0])
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += (father+'有'+arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += (father+'有'+arr[len(arr) - 2])
                    #respons_str += (father+'有'+target[0])

                else:
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += ('和'+target[0])
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += ('和'+arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += ('和'+arr[len(arr) - 2])
                    #respons_str += '和'+target[0]

            index = index + 1
        if count_yes>0:
            respons_str += ("。\n")

        index = 0
        for target in room_in_question[1:]:
            #print(index)
            if ans[index] == 0:
                if count_no == 0:
                    count_no = count_no+1
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += (father+'没有'+target[0])
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += (father+'没有'+arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += (father+'没有'+arr[len(arr) - 2])

                    #respons_str += (father + '没有' + target[0])

                else:
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += '和'+target[0]
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += '和'+arr[len(arr) - 1]
                        else:
                            # print(len(arr),"lll")
                            respons_str += '和'+arr[len(arr) - 2]
                    #respons_str += '和' + target[0]

            index = index + 1
        if count_no > 0:
            respons_str += ("。\n")


        return respons_str

    def answer_room_room_a(cls, entity_dict, graph):
        c = 0
        room_in_question = entity_dict['room'][0][0]
        ans=rdfPrepare.rdf_queryreverse_relation(room_in_question,'rel_part_of_room','room',graph)
        #print(ans)
        if len(ans)==0:
            return "很抱歉，"+room_in_question+"不包含其他馆室。"
        else:
            respons_str = room_in_question+"有:\n"
            for i in ans[:-1]:
                if i.find('厕所') != -1 or i.find('梯')!=-1 or i.find('卫生间') != -1:
                    continue
                c = c+1
                if i.find('_') == -1:
                    #if i == '5':
                        #print("5_-1")
                    respons_str += i+"\n"
                else:
                    arr = i.split('_')
                    if len(arr) == 3:
                        if i == '总馆北区_F4人工复制处_5':
                            respons_str += arr[len(arr) - 2] + "\n"
                        else:
                            respons_str += arr[len(arr) - 1] + "\n"
                    else:
                        #if (arr[len(arr) - 2] == '5'):
                        #    print(i, "5")
                        #print(len(arr),arr[len(arr) - 2],i)
                        respons_str += arr[len(arr) - 2] + "\n"
            last = ans[len(ans)-1]
            if last.find('厕所') != -1 or last.find('梯') != -1 or last.find('卫生间') != -1:
                return respons_str+'总共有'+str(c)+"间馆室。\n"
            c=c+1
            if last.find('_') == -1:
                #print(last,"-1")
                respons_str += last + "\n"
            else:
                arr = last.split('_')
                if len(arr) == 3:
                    #print(len(arr),"which")
                    respons_str += arr[len(arr) - 1] + "\n"
                else:
                    #print(len(arr),"lll")
                    respons_str += arr[len(arr) - 2] + "\n"
                #respons_str += arr[len(arr)-2]

            return respons_str+'总共有'+str(c)+"间馆室。\n"

    def answer_floor_room_a(cls, entity_dict, graph):
        count = 0
        floor_in_question = entity_dict['floor'][0][0]
        ans=rdfPrepare.rdf_queryreverse_relation(floor_in_question,'rel_part_of_floor','room',graph)
        #print(ans)
        if len(ans)==0:
            return "很抱歉，"+floor_in_question+"不包含其他馆室。"
        else:
            respons_str = floor_in_question+"有:\n"
            for i in ans[:-1]:
                if i.find('厕所') != -1 or i.find('梯')!=-1 or i.find('卫生间') != -1:
                    continue
                count = count+1
                if i.find('_') == -1:
                    #print(i,"-1")
                    respons_str += i + "\n"
                else:
                    arr = i.split('_')
                    if len(arr) == 3:
                        if i == '总馆北区_F4人工复制处_5':
                            respons_str += arr[len(arr) - 2] + "\n"
                        else:
                            #print(i,arr[len(arr) - 1], "3")
                            respons_str += arr[len(arr) - 1] + "\n"
                    else:
                        #print(i, arr[len(arr) - 2], "4")
                        respons_str += arr[len(arr) - 2] + "\n"
            last = ans[len(ans) - 1]
            if last.find('厕所') != -1 or last.find('梯') != -1 or last.find('卫生间') != -1:
                return respons_str+'总共有'+str(count)+"间馆室。\n"
            count = count + 1
            #print(last)
            if last.find('_') == -1:
                print(last)
                respons_str += last + "\n"
            else:
                arr = last.split('_')
                if len(arr) == 3:
                    # print(len(arr),"which")
                    respons_str += arr[len(arr) - 1] + "\n"
                else:
                    # print(len(arr),"lll")
                    respons_str += arr[len(arr) - 2] + "\n"

            return respons_str+'总共有'+str(count)+"间馆室。\n"


    #楼层馆室
    def answer_room_floor_l(cls,entity_dict,graph):
        room_in_question = entity_dict['room']
        floor_in_question = entity_dict['floor']

        #print(room_in_question,floor_in_question)
        respons_str = ''

        ans=[]
        count_yes = 0
        count_no = 0
        #print(len(room_in_question[:-1]))
        for target in room_in_question:
            flag = 0
            if (len(target)) == 0:
                continue
            for t in target:
                if (rdfPrepare.rdf_query_relation(t, "rel_part_of_floor", graph)[0] == floor_in_question[0][0]):
                    flag = 1
            ans.append(flag)

        #print(ans)

        index = 0
        for target in room_in_question:

            if (len(target)) == 0:
                continue
            if ans[index]:
                if count_yes == 0:
                    count_yes = count_yes + 1
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += (target[0])
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += (arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += (arr[len(arr) - 2])
                    #respons_str += target[0]

                else:
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += ('和' + target[0])
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += ('和' + arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += ('和' + arr[len(arr) - 2])
            index = index + 1
        if count_yes>0:
            respons_str += ('在' + floor_in_question[0][0]+"。\n")

        index = 0
        for target in room_in_question:
            if (len(target)) == 0:
                continue
            if ans[index] == 0:
                if count_no == 0:
                    count_no = count_no+1
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += (target[0])
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += (arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += (arr[len(arr) - 2])

                else:
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += ('和' + target[0])
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += ('和' + arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += ('和' + arr[len(arr) - 2])

            index = index + 1
        if count_no > 0:
            respons_str += ('不在' + floor_in_question[0][0]+"。\n")


        return respons_str+'\n'

    def answer_room_floor_h(cls,entity_dict,graph):
        room_in_question = entity_dict['room']
        floor_in_question = entity_dict['floor'][0][0]
        #print(room_in_question,floor_in_question)
        respons_str = ''

        ans=[]

        #print(father)
        count_yes = 0
        count_no = 0
        #print(len(room_in_question[:-1]))
        for target in room_in_question:
            flag = 0
            if (len(target)) == 0:
                continue
            for t in target:
                if (rdfPrepare.rdf_query_relation(t, "rel_part_of_floor", graph)[0] == floor_in_question[0][0]):
                    flag = 1
            ans.append(flag)


        index = 0
        for target in room_in_question:
            if (len(target)) == 0:
                continue
            if ans[index]:
                if count_yes == 0:
                    count_yes = count_yes + 1
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += (floor_in_question+'有'+target[0])
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += (floor_in_question+'有'+arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += (floor_in_question+'有'+arr[len(arr) - 2])
            else:
                if target[0].find('_') == -1:
                    # print(last,"-1")
                    respons_str += ('和' + target[0])
                else:
                    arr = target[0].split('_')
                    if len(arr) == 3:
                        # print(len(arr),"which")
                        respons_str += ('和' + arr[len(arr) - 1])
                    else:
                        # print(len(arr),"lll")
                        respons_str += ('和' + arr[len(arr) - 2])
            '''
            if ans[index]:
                if count_yes == 0:
                    count_yes = count_yes + 1
                    respons_str += (floor_in_question+'有'+target[0])

                else:
                    respons_str += '和'+target[0]
            '''

            index = index + 1
        if count_yes>0:
            respons_str += ("。\n")

        index = 0
        for target in room_in_question:
            if (len(target)) == 0:
                continue
            #print(index)
            if ans[index] == 0:
                if count_no == 0:
                    count_no = count_no+1
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += (floor_in_question+'没有'+target[0])
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += (floor_in_question+'没有'+arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += (floor_in_question+'没有'+arr[len(arr) - 2])

                    #respons_str += (father + '没有' + target[0])

                else:
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += '和'+target[0]
                    else:
                        arr = target[0].split('_')
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += '和'+arr[len(arr) - 1]
                        else:
                            # print(len(arr),"lll")
                            respons_str += '和'+arr[len(arr) - 2]

            '''
            if ans[index] == 0:
                if count_no == 0:
                    count_no = count_no+1

                    respons_str += (floor_in_question + '没有' + target[0])

                else:
                    respons_str += '和' + target[0]
            '''

            index = index + 1
        if count_no > 0:
            respons_str += ("。\n")


        return respons_str

    #资源楼层
    def answer_res_floor_h(cls,entity_dict,graph):
        res_in_question = entity_dict['res']
        respons_str = ''
        ans = []
        floor_in_question = entity_dict['floor'][0][0]
        room = rdfPrepare.rdf_queryreverse_relation(floor_in_question, 'rel_part_of_floor', 'room', graph)
        # print(room)
        for i in range(len(res_in_question)):

            # print(r)
            flag = 0
            for r in room:
                # print(r,res_in_question[i][0],rdfPrepare.rdf_query_relation(res_in_question[i][0], 'rel_part_of_room', graph)[0])
                if (r in rdfPrepare.rdf_query_relation(res_in_question[i][0], 'rel_part_of_room', graph)):
                    # print('ysssssssss')
                    ans.append(1)
                    flag = 1
                    break
                # else:
                #    print('asdfghjj',r, res_in_question[i][0],
                #          rdfPrepare.rdf_query_relation(res_in_question[i][0], 'rel_part_of_room', graph)[0])
            if flag == 0:
                ans.append(0)
        count_yes = 0
        count_no = 0
        index = 0
        for target in res_in_question:
            if (len(target)) == 0:
                continue
            if ans[index]:
                if count_yes == 0:
                    count_yes = count_yes + 1
                    if target[0].find('_') == -1:
                        respons_str += (floor_in_question+'有'+target[0])
                    else:
                        arr = target[0].split('_')
                        respons_str += (floor_in_question+'有'+arr[len(arr) - 1])


                else:
                    if target[0].find('_') == -1:
                        respons_str += ('和'+target[0])
                    else:
                        arr = target[0].split('_')
                        respons_str += ('和'+arr[len(arr) - 1])
                    #respons_str += '和'+target[0]

            index = index + 1
        if count_yes>0:
            respons_str += ("。\n")

        index = 0
        for target in res_in_question:
            if (len(target)) == 0:
                continue
            #print(index)
            if ans[index] == 0:
                if count_no == 0:
                    count_no = count_no+1
                    if target[0].find('_') == -1:
                        respons_str += (floor_in_question+'没有'+target[0])
                    else:
                        arr = target[0].split('_')
                        respons_str += (floor_in_question+'没有'+arr[len(arr) - 1])

                    #respons_str += (floor_in_question + '没有' + target[0])

                else:
                    if target[0].find('_') == -1:
                        respons_str += ('和'+target[0])
                    else:
                        arr = target[0].split('_')
                        respons_str += ('和'+arr[len(arr) - 1])
                    #respons_str += '和' + target[0]

            index = index + 1
        if count_no > 0:
            respons_str += ("。\n")
        return respons_str


    def answer_res_floor_l(cls,entity_dict,graph):
        #print("ssssss")
        res_in_question = entity_dict['res']
        respons_str = ''
        ans=[]
        floor_in_question = entity_dict['floor'][0][0]
        room = rdfPrepare.rdf_queryreverse_relation(floor_in_question, 'rel_part_of_floor', 'room', graph)
        print(room)
        for i in range(len(res_in_question)):

            #print(r)
            flag = 0
            for r in room:
                a=rdfPrepare.rdf_query_relation(res_in_question[i][0], 'rel_part_of_room', graph)
                #print(r,a)
                #print(r,res_in_question[i][0],rdfPrepare.rdf_query_relation(res_in_question[i][0], 'rel_part_of_room', graph)[0])
                if r in (rdfPrepare.rdf_query_relation(res_in_question[i][0], 'rel_part_of_room', graph)):
                    #print('ysssssssss')
                    ans.append(1)
                    flag = 1
                    break
                #else:
                #    print('asdfghjj',r, res_in_question[i][0],
                #          rdfPrepare.rdf_query_relation(res_in_question[i][0], 'rel_part_of_room', graph)[0])
            if flag == 0:
                ans.append(0)

        count_yes = 0
        count_no = 0

        index = 0
        for target in res_in_question:
            if (len(target)) == 0:
                continue
            if ans[index]:
                if count_yes == 0:
                    count_yes = count_yes + 1
                    if target[0].find('_') == -1:
                        respons_str += (target[0])
                    else:
                        arr = target[0].split('_')
                        respons_str += (arr[len(arr) - 1])

                else:
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += ('和' + target[0])
                    else:
                        arr = target[0].split('_')
                        respons_str += ('和' + arr[len(arr) - 1])
            index = index + 1
        if count_yes>0:
            respons_str += ('在' + floor_in_question+"。\n")

        index = 0
        for target in res_in_question:
            if (len(target)) == 0:
                continue
            #print(index)
            if ans[index] == 0:
                if count_no == 0:
                    count_no = count_no+1
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += (target[0])
                    else:
                        arr = target[0].split('_')
                        respons_str += (arr[len(arr) - 1])


                else:
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += ('和' + target[0])
                    else:
                        arr = target[0].split('_')
                        respons_str += ('和' + arr[len(arr) - 1])

            index = index + 1
        if count_no > 0:
            respons_str += ('不在' + floor_in_question+"。\n")


        return respons_str

    #资源馆室
    def answer_res_room_h(cls,entity_dict,graph):
        res_in_question = entity_dict['res']
        room_in_question = entity_dict['room'][0][0]
        #print(room_in_question)
        #print(room_in_question)
        respons_str = ''

        ans=[]

        #print(father)
        count_yes = 0
        count_no = 0
        #print(len(room_in_question[:-1]))
        for target in res_in_question:
            if (len(target)) == 0:
                continue
            if (len(rdfPrepare.rdf_query_relation(target[0], "rel_part_of_room", graph))<=0):
                ans.append(0)
                continue
            if (rdfPrepare.rdf_query_relation(target[0], "rel_part_of_room", graph)[0] == room_in_question):
                ans.append(1)
            else :
                ans.append(0)
        #print(ans,res_in_question)

        index = 0
        for target in res_in_question:
            if (len(target)) == 0:
                continue
            if ans[index]:
                if count_yes == 0:
                    count_yes = count_yes + 1
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += (room_in_question+'有'+target[0])
                    else:
                        arr = target[0].split('_')
                        respons_str += (room_in_question + '有' + arr[len(arr) - 1])
                        '''
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += (room_in_question+'有'+arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += (room_in_question+'有'+arr[len(arr) - 2])
                        '''
                else:
                    if target[0].find('_') == -1:
                    # print(last,"-1")
                        respons_str += ('和' + target[0])
                    else:
                        arr = target[0].split('_')
                        respons_str += ('和' + arr[len(arr) - 1])
                    '''
                    if len(arr) == 3:
                        # print(len(arr),"which")
                        respons_str += ('和' + arr[len(arr) - 1])
                    else:
                        # print(len(arr),"lll")
                        respons_str += ('和' + arr[len(arr) - 2])
                    '''
            '''
            if ans[index]:
                if count_yes == 0:
                    count_yes = count_yes + 1
                    respons_str += (room_in_question+'有'+target[0])

                else:
                    respons_str += '和'+target[0]
            '''

            index = index + 1
        if count_yes>0:
            respons_str += ("。\n")

        index = 0
        for target in res_in_question:
            if (len(target)) == 0:
                continue
            #print(index)
            if ans[index] == 0:
                if count_no == 0:
                    count_no = count_no+1
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += (room_in_question+'没有'+target[0])
                    else:

                        arr = target[0].split('_')
                        respons_str += (room_in_question + '没有' + arr[len(arr) - 1])
                        '''
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += (room_in_question+'没有'+arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += (room_in_question+'没有'+arr[len(arr) - 2])
                        '''

                    #respons_str += (father + '没有' + target[0])

                else:
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += '和'+target[0]
                    else:
                        arr = target[0].split('_')
                        respons_str += ('和' + arr[len(arr) - 1])
                        '''
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += '和'+arr[len(arr) - 1]
                        else:
                            # print(len(arr),"lll")
                            respons_str += '和'+arr[len(arr) - 2]
                        '''
            '''
            if ans[index] == 0:
                if count_no == 0:
                    count_no = count_no+1

                    respons_str += (room_in_question + '没有' + target[0])

                else:
                    respons_str += '和' + target[0]
            '''

            index = index + 1
        if count_no > 0:
            respons_str += ("。\n")
        return respons_str


    def answer_res_room_l(cls,entity_dict,graph):
        res_in_question = entity_dict['res']
        room_in_question = entity_dict['room']
        #print(res_in_question)
        #print(room_in_question)
        respons_str = ''

        ans=[]
        count_yes = 0
        count_no = 0
        #print(len(room_in_question[:-1]))
        for target in res_in_question:
            if (len(target)) == 0:
                continue
            if (len(rdfPrepare.rdf_query_relation(target[0], "rel_part_of_room", graph))<=0):
                ans.append(0)
                continue
            if (rdfPrepare.rdf_query_relation(target[0], "rel_part_of_room", graph)[0] == room_in_question[0][0]):
                ans.append(1)
            else :
                ans.append(0)
        #print(ans)

        index = 0
        for target in res_in_question:
            if (len(target)) == 0:
                continue
            if ans[index]:
                if count_yes == 0:
                    count_yes = count_yes + 1
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += (target[0])
                    else:
                        arr = target[0].split('_')
                        respons_str += (arr[len(arr) - 1])
                        '''
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += (arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += (arr[len(arr) - 2])
                        '''
                    #respons_str += target[0]

                else:
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += ('和' + target[0])
                    else:
                        arr = target[0].split('_')
                        respons_str += ('和' + arr[len(arr) - 1])
                        '''
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += ('和' + arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += ('和' + arr[len(arr) - 2])
                        '''
            '''
            if ans[index]:
                if count_yes == 0:
                    count_yes = count_yes + 1
                    respons_str += target[0]

                else:
                    respons_str += '和'+target[0]
            '''

            index = index + 1
        if count_yes>0:
            respons_str += ('在' + room_in_question[0][0]+"。")

        index = 0
        for target in res_in_question:
            if (len(target)) == 0:
                continue
            #print(index)
            if ans[index] == 0:
                if count_no == 0:
                    count_no = count_no+1
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += (target[0])
                    else:
                        arr = target[0].split('_')
                        respons_str += (arr[len(arr) - 1])
                        '''
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += (arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += (arr[len(arr) - 2])
                        '''

                else:
                    if target[0].find('_') == -1:
                        # print(last,"-1")
                        respons_str += ('和' + target[0])
                    else:
                        arr = target[0].split('_')
                        respons_str += ('和' + arr[len(arr) - 1])
                        '''
                        if len(arr) == 3:
                            # print(len(arr),"which")
                            respons_str += ('和' + arr[len(arr) - 1])
                        else:
                            # print(len(arr),"lll")
                            respons_str += ('和' + arr[len(arr) - 2])
                        '''
            '''
            if ans[index] == 0:
                if count_no == 0:
                    count_no = count_no+1
                    respons_str += target[0]

                else:
                    respons_str += '和' + target[0]
            '''

            index = index + 1
        if count_no > 0:
            respons_str += ('不在' + room_in_question[0][0]+"。")


        return respons_str+'\n'

    def answer_room_res_a(cls, entity_dict, graph):
        respons_str = ''
        room_in_question = entity_dict['room'][0][0]
        room = rdfPrepare.rdf_queryreverse_relation(room_in_question,'rel_part_of_room','room',graph)
        #print(room)
        if len(room) == 0:
            res=rdfPrepare.rdf_queryreverse_relation(room_in_question,'rel_part_of_room','resource',graph)
            #print(res)
            if len(res)==0:
                return "很抱歉，"+room_in_question+"不包含任何资源。\n"
            else:
                respons_str += room_in_question+"有:\n"
                for i in res[:-1]:

                    if i.find('_') == -1:
                        #print(i,"-1")
                        respons_str += i + "\n"
                    else:
                        arr = i.split('_')
                        respons_str += arr[len(arr) - 1] + "\n"

                last = res[len(res) - 1]

                #print(last)
                if last.find('_') == -1:
                    #print(last)
                    respons_str += last + "\n"
                else:
                    arr = last.split('_')
                    respons_str += arr[len(arr) - 1] + "\n"
        else:
            for r in room:
                subroom = ''
                if r.find('厕所') != -1 or r.find('梯')!=-1 or r.find('卫生间') != -1:
                    continue
                if r.find('_') == -1:
                    # print(last,"-1")
                    subroom = r
                    respons_str += ('\n'+room_in_question+'包含' + r+'，其中有的资源如下：\n')
                else:
                    arr = r.split('_')
                    if len(arr) == 3:
                        subroom = arr[len(arr) - 1]
                        respons_str += ('\n'+room_in_question+'包含' + arr[len(arr) - 1]+'，其中有的资源如下：\n')
                    else:
                        subroom = arr[len(arr) - 2]
                        respons_str += ('\n'+room_in_question+'包含' + arr[len(arr) - 2]+'，其中有的资源如下：\n')
                mulres = rdfPrepare.rdf_queryreverse_relation(r, 'rel_part_of_room', 'resource', graph)
                if len(mulres) == 0:
                    respons_str += subroom + "不包含任何资源。\n"
                else:

                    for subres in mulres:

                        if subres.find('_') == -1:
                            # print(i,"-1")
                            respons_str += subres + "\n"
                        else:
                            arr = subres.split('_')
                            respons_str += arr[len(arr) - 1] + "\n"

        return respons_str
    def answer_floor_res_a(cls, entity_dict, graph):
        respons_str = ''
        floor_in_question = entity_dict['floor'][0][0]
        room = rdfPrepare.rdf_queryreverse_relation(floor_in_question,'rel_part_of_floor','room',graph)
        for r in room:
            subroom = ''
            if r.find('厕所') != -1 or r.find('梯')!=-1 or r.find('卫生间') != -1:
                continue
            if r.find('_') == -1:
                # print(last,"-1")
                subroom = r
                respons_str += ('\n'+floor_in_question+'包含' + r+'，其中有的资源如下：\n')
            else:
                arr = r.split('_')
                if len(arr) == 3:
                    subroom = arr[len(arr) - 1]
                    respons_str += ('\n'+floor_in_question+'包含' + arr[len(arr) - 1]+'，其中有的资源如下：\n')
                else:

                    subroom = arr[len(arr) - 2]
                    respons_str += ('\n'+floor_in_question+'包含' + arr[len(arr) - 2]+'，其中有的资源如下：\n')
            mulres = rdfPrepare.rdf_queryreverse_relation(r, 'rel_part_of_room', 'resource', graph)
            if len(mulres) == 0:
                respons_str += subroom + "不包含任何资源。\n"
            else:

                for subres in mulres:

                    if subres.find('_') == -1:
                            # print(i,"-1")
                        respons_str += subres + "\n"
                    else:
                        arr = subres.split('_')
                        respons_str += arr[len(arr) - 1] + "\n"

        return respons_str
    def answer_room_room_or_res_a(cls, entity_dict, graph):
        respons_str = ''
        room_in_question = entity_dict['room'][0][0]
        room = rdfPrepare.rdf_queryreverse_relation(room_in_question,'rel_part_of_room','room',graph)
        if len(room) == 0:
            res=rdfPrepare.rdf_queryreverse_relation(room_in_question,'rel_part_of_room','resource',graph)
            print(res)
            if len(res)==0:
                return "很抱歉，"+room_in_question+"不包含任何资源。\n"
            else:
                respons_str += room_in_question+"有:\n"
                for i in res[:-1]:

                    if i.find('_') == -1:
                        #print(i,"-1")
                        respons_str += i + "\n"
                    else:
                        arr = i.split('_')
                        respons_str += arr[len(arr) - 1] + "\n"

                last = res[len(res) - 1]

                #print(last)
                if last.find('_') == -1:
                    #print(last)
                    respons_str += last + "\n"
                else:
                    arr = last.split('_')
                    respons_str += arr[len(arr) - 1] + "\n"
        else:
            respons_str += room_in_question + "有:\n"
            for r in room:
                subroom = ''
                if r.find('厕所') != -1 or r.find('梯')!=-1 or r.find('卫生间') != -1:
                    continue
                if r.find('_') == -1:
                    # print(last,"-1")
                    subroom = r
                    respons_str += (r+'\n')
                else:
                    arr = r.split('_')
                    if len(arr) == 3:
                        subroom = arr[len(arr) - 1]
                        respons_str += (arr[len(arr) - 1]+'\n')
                    else:
                        subroom = arr[len(arr) - 2]
                        respons_str += (arr[len(arr) - 2]+'\n')
        return respons_str

    def answer_count_res(cls, entity_dict, graph):
        res_in_question = entity_dict['res']
        #print(res_in_question)
        count = rdfPrepare.rdf_query_count(res_in_question[0][0], graph)
        #print(count)
        respons_str = res_in_question[0][0] + '一共有' + str(count[0]) + '本。\n'

        return respons_str

    def answer_count_floor(cls, entity_dict, graph):
        print(entity_dict)
        respons_str = ''
        if(len(entity_dict['room'][0])>1):
            temp = rdfPrepare.rdf_queryreverse_relation(entity_dict['room'][0][0], 'rel_part_of_room', 'room', graph)
            if(len(temp)>0):
                for room in entity_dict['room'][0]:

                    # print(entity_dict['room'],room_in_question)
                    floor = rdfPrepare.rdf_queryreverse_relation(room, 'rel_part_of_room', 'floor', graph)
                    if len(floor) > 0:

                        respons_str += room + "一共有" + str(len(floor)) + '层。\n'
                    else:
                        respons_str += '只有一层。\n'
            else:

                r = entity_dict['room'][0][0]
                if r.find('_') == -1:
                    # print(last,"-1")

                    respons_str += (r + '一共有'+str(len(entity_dict['room'][0]))+'层。\n')
                else:
                    arr = r.split('_')
                    if len(arr) == 3:

                        respons_str += (arr[len(arr) - 1] + '一共有'+str(len(entity_dict['room'][0]))+'层。\n')
                    else:

                        respons_str += (arr[len(arr) - 2] + '一共有'+str(len(entity_dict['room'][0]))+'层。\n')
            return respons_str

        room_in_question = entity_dict['room'][0][0]
        #print(entity_dict['room'],room_in_question)
        floor = rdfPrepare.rdf_queryreverse_relation(room_in_question, 'rel_part_of_room', 'floor', graph)
        if len(floor)>0:

            respons_str += room_in_question+"一共有"+str(len(floor))+'层。\n'
        else :
            respons_str += '只有一层。\n'
        return respons_str

    def answer_floor_count_room(cls, entity_dict, graph):
        room_in_question = entity_dict['room']
        floor_in_question = entity_dict['floor'][0][0]
        respons_str = ''
        #print(room_in_question)
        for target in room_in_question:
            count = 0
            for t in target:
                #print(t,floor_in_question)
                if (rdfPrepare.rdf_query_relation(t, "rel_part_of_floor", graph)[0] == floor_in_question):
                    count = count+1
                    #print(t, floor_in_question,count)
            #arr.append(count)
            if count == 0:

                if target[0].find('_') == -1:
                    # print(last,"-1")
                    respons_str += (floor_in_question + '没有' + target[0]+"。\n")
                else:
                    arr = target[0].split('_')
                    if len(arr) == 3:
                        # print(len(arr),"which")
                        respons_str += (floor_in_question + '没有' + arr[len(arr) - 1]+"。\n")
                    else:
                        # print(len(arr),"lll")
                        respons_str += (floor_in_question + '没有' + arr[len(arr) - 2]+"。\n")
            else:
                if target[0].find('_') == -1:
                    # print(last,"-1")
                    respons_str += (floor_in_question + '一共有' + str(count) + '间'+target[0]+"。\n")
                else:
                    arr = target[0].split('_')
                    if len(arr) == 3:
                        # print(len(arr),"which")
                        respons_str += (floor_in_question + '一共有' + str(count) + '间'+ arr[len(arr) - 1]+"。\n")
                    else:
                        # print(len(arr),"lll")
                        respons_str += (floor_in_question + '一共有' + str(count) + '间'+ arr[len(arr) - 2]+"。\n")
                #respons_str += (floor_in_question + '一共有' + str(count) + '间'+'。\n')
        return respons_str

    def answer_res_res_h(cls, entity_dict, question_str,graph):

            entity_count = 1
            arr = []
            if len(entity_dict['res']) > 0:
                for i in entity_dict['res']:
                    if len(i) == 0:
                        continue
                    index = question_str.find(i[0])
                    if index == -1:
                        index = len(entity_dict['res']) - entity_count
                        entity_count = entity_count + 1
                    arr.append(index)
                # print(arr)
                arr_index = np.argsort(np.array(arr))
                # print(arr_index)
                entity_dict2 = []
                for i in entity_dict['res']:
                    if len(i) == 0:
                        continue
                    entity_dict2.append(i)

                for i in range(len(entity_dict['res'])):
                    if len(entity_dict['res'][i]) == 0:
                        continue
                    # print(arr_index[i],entity_dict2[arr_index[i]])
                    entity_dict['res'][i] = entity_dict2[arr_index[i]]
            res_in_question = entity_dict['res']
            #print(res_in_question)
            respons_str = ''

            ans = []
            father = res_in_question[0][0]
            # print(father)
            count_yes = 0
            count_no = 0
            # print(len(room_in_question[:-1]))
            for target in res_in_question[1:]:
                flag = 0
                if (len(target)) == 0:
                    continue
                for t in target:
                    if (rdfPrepare.rdf_query_relation(t, "rel_part_of_source", graph)[0] == father):
                        flag = 1
                ans.append(flag)

            # print(ans)

            index = 0
            for target in res_in_question[1:]:
                if ans[index]:
                    if count_yes == 0:
                        count_yes = count_yes + 1
                        if target[0].find('_') == -1:
                            # print(last,"-1")
                            respons_str += (father + '包括' + target[0])
                        else:
                            arr = target[0].split('_')
                            respons_str += (father + '包括' + arr[len(arr) - 1])


                    else:
                        if target[0].find('_') == -1:
                            # print(last,"-1")
                            respons_str += ('和' + target[0])
                        else:
                            arr = target[0].split('_')
                            respons_str += ('和' + arr[len(arr) - 1])


                index = index + 1
            if count_yes > 0:
                respons_str += ("。\n")

            index = 0
            for target in res_in_question[1:]:
                # print(index)
                if ans[index] == 0:
                    if count_no == 0:
                        count_no = count_no + 1
                        if target[0].find('_') == -1:
                            # print(last,"-1")
                            respons_str += (father + '不包括' + target[0])
                        else:
                            arr = target[0].split('_')
                            respons_str += (father + '不包括' + arr[len(arr) - 1])


                    else:
                        if target[0].find('_') == -1:
                            # print(last,"-1")
                            respons_str += '和' + target[0]
                        else:
                            arr = target[0].split('_')
                            respons_str += '和' + arr[len(arr) - 1]


                index = index + 1
            if count_no > 0:
                respons_str += ("。\n")

            return respons_str

    def answer_res_res_a(cls, entity_dict, graph):
        res_in_question = entity_dict['res'][0][0]
        #print(res_in_question)
        ans=rdfPrepare.rdf_queryreverse_relation(res_in_question,'rel_part_of_source','resource',graph)
        #print(ans)
        if len(ans)==0:
            return "很抱歉，"+res_in_question+"不包括其他资源。"
        else:
            respons_str = res_in_question+"有:\n"
            for i in ans:
                if i.find('_') == -1:
                    respons_str += i+"\n"
                else:
                    arr = i.split('_')
                    respons_str += arr[len(arr) - 1] + "\n"

        return respons_str

    def answer_room_count_room(cls, entity_dict, question_str,graph):
        entity_count = 1
        arr = []
        if len(entity_dict['room']) > 0:
            for i in entity_dict['room']:
                if len(i) == 0:
                    continue
                index = question_str.find(i[0])
                if index == -1:
                    index = len(entity_dict['room']) - entity_count
                    entity_count = entity_count + 1
                arr.append(index)
            # print(arr)
            arr_index = np.argsort(np.array(arr))
            # print(arr_index)
            entity_dict2 = []
            for i in entity_dict['room']:
                if len(i) == 0:
                    continue
                entity_dict2.append(i)

            for i in range(len(entity_dict['room'])):
                if len(entity_dict['room'][i]) == 0:
                    continue
                # print(arr_index[i],entity_dict2[arr_index[i]])
                entity_dict['room'][i] = entity_dict2[arr_index[i]]

        room_in_question = entity_dict['room'][1:]
        father = entity_dict['room'][0][0]
        respons_str = ''
        #print(room_in_question)
        for target in room_in_question:
            count = 0
            for t in target:
                #print(t,floor_in_question)
                if (rdfPrepare.rdf_query_relation(t, "rel_part_of_room", graph)[0] == father):
                    count = count+1
                    #print(t, floor_in_question,count)
            #arr.append(count)
            if count == 0:

                if target[0].find('_') == -1:
                    # print(last,"-1")
                    respons_str += (father + '没有' + target[0]+"。\n")
                else:
                    arr = target[0].split('_')
                    if len(arr) == 3:
                        # print(len(arr),"which")
                        respons_str += (father + '没有' + arr[len(arr) - 1]+"。\n")
                    else:
                        # print(len(arr),"lll")
                        respons_str += (father + '没有' + arr[len(arr) - 2]+"。\n")
            else:
                if target[0].find('_') == -1:
                    # print(last,"-1")
                    respons_str += (father + '一共有' + str(count) + '间'+target[0]+"。\n")
                else:
                    arr = target[0].split('_')
                    if len(arr) == 3:
                        # print(len(arr),"which")
                        respons_str += (father + '一共有' + str(count) + '间'+ arr[len(arr) - 1]+"。\n")
                    else:
                        # print(len(arr),"lll")
                        respons_str += (father + '一共有' + str(count) + '间'+ arr[len(arr) - 2]+"。\n")
                #respons_str += (floor_in_question + '一共有' + str(count) + '间'+'。\n')
        return respons_str








