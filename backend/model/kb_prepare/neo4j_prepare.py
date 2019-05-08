# -*- coding: utf-8 -*-

import os
import pandas as pd
import  py2neo
from py2neo import Node, Graph, Relationship
from pandas import DataFrame
import numpy as np
import xlrd
class Neo4jPrepare(object):


    @classmethod
    def __init__(cls):
        """建立连接"""

        link = Graph("bolt://127.0.0.1:7687", username="lin123", password="lin123")
        cls.graph = link

        """定义label"""
        cls.building = '馆区'
        cls.room = '馆室'
        cls.floor = '楼层'
        cls.resource = "资源"

        cls.graph.delete_all()

        """建图"""
        workbook = xlrd.open_workbook(r'../../resource/neo4j_libot.xlsx')
        cls.create_node(workbook)
        cls.create_relation(workbook)
        cls.room_list,cls.room_variant_list,cls.floor_list,cls.floor_variant_list,cls.area_list,cls.area_variant_list,cls.resource_list,cls.resource_variant_list=cls.get_all_varname()

        #print(cls.room_list,cls.area_variant_list,cls.resource_variant_list)

    '''
    属性查询
    '''
    @classmethod
    def get_property(cls,entity):

        cursor = cls.graph.run("match(n {office_name:{a}})return n",a=entity)
        print(cursor)
        cursor.forward()
        record = cursor.current()
        return (dict(record['n']))


    '''
    关系查询，直接关联
    '''

    @classmethod
    def get_relation(cls, entity, type):
        cursor = cls.graph.run("match(n {office_name:{a}})-[]->(b {type:{r}}) return b", a=entity,r=type)

        ans=[]
        while cursor.forward():

            record = cursor.current()
            ans.append(dict(record['b']))
            print(dict(record['b']))
        return ans

    '''
    关系查询，多级关联，最多两跳
    '''

    @classmethod
    def get_relation_mul(cls, entity, type):
        cursor = cls.graph.run("match(n {office_name:{a}})-[*..2]->(b {type:{r}}) return b", a=entity, r=type)

        ans = []
        while cursor.forward():

            record = cursor.current()
            ans.append(dict(record['b']))
            print(dict(record['b']))
        return ans


    '''
    逆向关系查询 直接关联
    '''

    @classmethod
    def get_reverse_relation(cls, entity, type):
        cursor = cls.graph.run("match(n {office_name:{a}})<-[]-(b {type:{r}}) return b", a=entity, r=type)
        #cursor = cls.graph.run("match(n{office_name: '数字共享空间'}) < -[] - (b {type:'资源'})return b")

        ans = []
        while cursor.forward():

            record = cursor.current()
            ans.append(dict(record['b']))
            print(dict(record['b']))
        return ans

    '''
    逆向关系查询 多级关联 最多两跳
    '''

    @classmethod
    def get_reverse_relation_mul(cls, entity, type):
        #print(entity,type)
        cursor = cls.graph.run("match(n {office_name:{a}})<-[*..2]-(b {type:{r}}) return b", a=entity, r=type)
        #cursor = cls.graph.run("match(n {office_name:{a}})<-[*]-(b {type:{r}}) return b", a='总馆北区', r='资源')

        ans = []
        while cursor.forward():

            record = cursor.current()
            ans.append(dict(record['b']))
            #print(dict(record['b']))
        return ans

    '''
    查出所有的别名
    '''
    @classmethod
    def get_all_varname(cls):

        room_list=[]
        room_variant_list=[]
        floor_list=[]
        floor_variant_list=[]
        area_list=[]
        area_variant_list = []
        resource_list=[]
        resource_variant_list=[]

        '''
        馆室正名、别名
        '''
        cursor = cls.graph.run("match(n:`馆室`)return n.office_name as room ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            room_list.append(record['room'])
            #print(type(record[variant_name]))
            temp = record['variant_name'].split("，")
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            room_variant_list.append(temp)

        #print(room_list)
        #print(room_variant_list)

        '''
        楼层正名、别名
        '''
        cursor = cls.graph.run("match(n:`楼层`)return n.office_name as floor ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            floor_list.append(record['floor'])
            temp = record['variant_name'].split("，")
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            floor_variant_list.append(temp)

        #print(floor_list)
        #print(floor_variant_list)

        '''
        馆区正名、别名
        '''
        cursor = cls.graph.run("match(n:`馆区`)return n.office_name as area ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            area_list.append(record['area'])
            temp = record['variant_name'].split("，")
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            area_variant_list.append(temp)

        #print(area_list)
        #print(area_variant_list)

        '''
        资源正名、别名
        '''
        cursor = cls.graph.run("match(n:`资源`)return n.office_name as resource ,n.variant_name as variant_name")
        while cursor.forward():
            record = dict(cursor.current())
            resource_list.append(record['resource'])
            temp = record['variant_name'].split("，")
            temp = sorted(temp, key=lambda i: len(i), reverse=True)
            resource_variant_list.append(temp)

        #print(resource_list)
        #print(resource_variant_list)

        return room_list,room_variant_list,floor_list,floor_variant_list,area_list,area_variant_list,resource_list,resource_variant_list

    @classmethod
    def repalce_question(cls, question):

        entity_dict={}

        offical_temp=[]
        for var_index in range(len(cls.resource_variant_list)):
            sub_var = cls.resource_variant_list[var_index]
            #print(sub_var)
            for sub_name in sub_var:
                if sub_name in question:
                    offical_temp.append(cls.resource_list[var_index])
                    question = question.replace(sub_name, 'RES')
                    break
        entity_dict['res'] = offical_temp

        offical_temp = []
        for var_index in range(len(cls.floor_variant_list)):
            sub_var = cls.floor_variant_list[var_index]
            #print(sub_var)
            for sub_name in sub_var:
                if sub_name in question:
                    offical_temp.append(cls.floor_list[var_index])
                    question = question.replace(sub_name, 'FLOOR')
                    break
        entity_dict['floor'] = offical_temp

        offical_temp = []
        for var_index in range(len(cls.room_variant_list)):
            sub_var = cls.room_variant_list[var_index]
            #print(sub_var)
            for sub_name in sub_var:
                if sub_name in question:
                    offical_temp.append(cls.room_list[var_index])
                    question = question.replace(sub_name, 'ROOM')
                    break

        for var_index in range(len(cls.area_variant_list)):
            sub_var = cls.area_variant_list[var_index]
            #print(sub_var)
            for sub_name in sub_var:
                if sub_name in question:
                    offical_temp.append(cls.area_list[var_index])
                    question = question.replace(sub_name, 'ROOM')
                    break
        entity_dict['room'] = offical_temp
        #print(entity_dict)
        #print(question)
        return question,entity_dict




    @classmethod
    def create_node(cls, workbook):
        """建立馆室节点"""
        room_sheet = workbook.sheet_by_index(0)
        for i in range(1,room_sheet.nrows):
            row = room_sheet.row_values(i)
            name=row[0]
            if row[0].find("_") != -1:
                name_arr = row[0].split("_")
                if len(name_arr)>=3:
                    name = name_arr[2]


            room_node = Node(cls.room,type=cls.room,name=name,office_name=row[0],variant_name=row[1],position=row[2],service=row[3],
                             open_date=row[4],phone=row[5],
                             monday_open=row[6],monday_borrow=row[7],
                             tuseday_open=row[8],tuseday_borrow=row[9],
                             wednesday_open=row[10],wednesday_borrow=row[11],
                             thursday_open=row[12],thursday_borrow=row[13],
                             friday_open=row[14], friday_borrow=row[15],
                             saturday_open=row[16], saturday_borrow=row[17],
                             sunday_open=row[18], sunday_borrow=row[19],
                             #area=row[20],floor=row[21],
                             certification=row[22])
            cls.graph.create(room_node)



        """建立馆区节点"""
        building_sheet = workbook.sheet_by_index(1)
        for i in range(1, building_sheet.nrows):
            row = building_sheet.row_values(i)
            name = row[0]
            #print(name)
            building_node = Node(cls.building, type=cls.building,name=name,
                                 office_name=row[0],
                                 variant_name=row[1])
            cls.graph.create(building_node)

        """建立楼层节点"""
        floor_sheet = workbook.sheet_by_index(3)
        for i in range(1, floor_sheet.nrows):
            row = floor_sheet.row_values(i)
            name = row[0]
            #print(name)
            floor_node = Node(cls.floor, type=cls.floor,name=name, office_name=row[0], variant_name=row[1],
                              #area=row[2],
                              upstair=row[3],downstair=row[4]
                              )
            cls.graph.create(floor_node)

        """建立资源节点"""
        resource_sheet = workbook.sheet_by_index(2)
        for i in range(1, resource_sheet.nrows):
            row = resource_sheet.row_values(i)
            name = row[0]
            if row[0].find("_") != -1:
                name = row[0].split("_")[1]
            # print(name)
            resource_node = Node(cls.resource, type=cls.resource,name=name, office_name=row[0], variant_name=row[1], describe=row[2], count=row[3],
                              #room=row[4],
                              belong=row[5])
            cls.graph.create(resource_node)

    @classmethod
    def create_relation(cls, workbook):
        """建立馆室联系"""

        room_sheet = workbook.sheet_by_index(0)
        for i in range(1, room_sheet.nrows-5):
            try:
                row = room_sheet.row_values(i)
                #print(self.graph.find_one(label=self.building, property_key='area', property_value=row[20]),row[20])
                rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                   property_value=row[0]), "处于",
                               cls.graph.find_one(label=cls.building, property_key='office_name', property_value=row[20]))
                cls.graph.create(rel)
                if row[21].find("，"):
                    floor_arr = row[21].split("，")
                    for sub_floor in floor_arr:
                        rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                               property_value=row[0]), "位于",
                                           cls.graph.find_one(label=cls.floor, property_key='office_name',
                                                               property_value=sub_floor))
                        cls.graph.create(rel)
            except AttributeError as e:
                print("1",row[0],e,row[20])
                print(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                   property_value=row[0]))
        for i in range(room_sheet.nrows - 5, room_sheet.nrows):
            try:
                row = room_sheet.row_values(i)
                #print(self.graph.find_one(label=self.building, property_key='area', property_value=row[20]),row[20])
                rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                   property_value=row[0]), "处于",
                               cls.graph.find_one(label=cls.room, property_key='office_name', property_value=row[20]))
                cls.graph.create(rel)
                rel = Relationship(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                       property_value=row[0]), "位于",
                                   cls.graph.find_one(label=cls.floor, property_key='office_name',
                                                       property_value=row[21]))
                cls.graph.create(rel)
            except AttributeError as e:
                a = 0
                #print("2",row[0],e,row[20])
                #print(cls.graph.find_one(label=cls.room, property_key='office_name',
                                                   #property_value=row[0]))
                #print(cls.graph.find_one(label=cls.room, property_key='office_name', property_value=row[20]))


        """建立楼层联系"""
        floor_sheet = workbook.sheet_by_index(3)
        for i in range(1, floor_sheet.nrows):
            try:
                row = floor_sheet.row_values(i)
                rel = Relationship(cls.graph.find_one(label=cls.floor, property_key='office_name',
                                                   property_value=row[0]), "处于",
                               cls.graph.find_one(label=cls.building, property_key='office_name', property_value=row[2]))
                cls.graph.create(rel)
            except AttributeError as e:
                a = 0
                #print("2",row[0],e,row[2])

        """建立资源联系"""
        floor_sheet = workbook.sheet_by_index(2)
        for i in range(1, floor_sheet.nrows):
            try:
                room_arr = []
                row = floor_sheet.row_values(i)
                #print(row[4])
                if row[4].find("，")!=-1:
                    room_arr = row[4].split("，")
                else:
                    room_arr.append(row[4])

                for sub_room in room_arr:
                    #print(sub_room,row[0])

                    rel = Relationship(cls.graph.find_one(label=cls.resource, property_key='office_name',
                                                       property_value=row[0]), "存放",
                                   cls.graph.find_one(label=cls.room, property_key='office_name', property_value=sub_room))
                    cls.graph.create(rel)
            except AttributeError as e:
                a = 0
                #print("3", row[0], e, row[4])
                #print(cls.graph.find_one(label=cls.room, property_key='office_name', property_value=row[4]))
                #print(self.graph.find_one(label=self.room, property_key='room', property_value=row[4]))





if __name__ == '__main__':

    a = Neo4jPrepare().get_relation('总馆北区一层','馆区')
    print(a)
    #print(q,e)
    #prepare.repalce_question("数字共享空间在总馆北区一层吗")


