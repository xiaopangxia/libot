# -*- coding: utf-8 -*-
# File: general_hub_1.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-09
import os
import sys
# 模块路径引用统一回退到Libbot目录下
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)

from model.question.entity_match import entityMatch
from model.question.entity_match2 import entityMatch2
from model.grapg_QA.json_bot import jsonBot
from model.grapg_QA.rdf_bot import rdfBot
from model import aiml_cn
from model.kb_prepare.rdf_prepare import rdfPrepare
import numpy as np
import time



class GeneralHub():
    """
    总控程序版本1
    """
    def __init__(self):
        self._aiml_kernal = aiml_cn.Kernel()
        self._aiml_kernal.learn('../../resource/template.aiml')
        self._aiml_kernal.learn('../../resource/contain_template.aiml')

    def question_answer_hub(self, question_str):
        """
        问答总控，基于aiml构建问题匹配器
        :param question_str:问句输入
        :return:
        """
        g = rdfPrepare.load_graph()
        question_replaced, entity_dict = entityMatch2.match_and_replace_all(question_str,g)
        # question_replaced, entity_dict = entityMatch.match_and_replace_all(question_str)
        '''
        arr = []
        if len(entity_dict['room']) > 0:
            for i in entity_dict['room']:
                if len(i) == 0:
                    continue
                index = question_str.find(i[0])
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
        '''
        aiml_respons = self._aiml_kernal.respond(question_replaced)
        if 'task_' in aiml_respons:
            #print("aiml_respons: ", str(aiml_respons))
            #print("entity_dict: ", str(entity_dict))
            graph_respons = rdfBot.task_response(aiml_respons,entity_dict,question_str,g)
            return graph_respons
        else:
            return aiml_respons



if __name__ == '__main__':
    gh = GeneralHub()
    # gh.question_answer_hub('少年儿童馆主题活动区电话啥啊？')
    # gh.question_answer_hub('少年儿童馆在哪啊？')
    # gh.question_answer_hub('少年儿童馆主题活动区电话啥啊？')
    # gh.question_answer_hub('会议论文在哪？')
    # gh.question_answer_hub('学位论文在哪？')
    # gh.question_answer_hub('香港书在哪个馆啊？')

    #gh.question_answer_hub('古籍馆什么时候开？')
    test_hub = GeneralHub()
    while True:
        question_str = input('User:')
        if question_str == 'exit':
            break
        else:
            print('Libot:', test_hub.question_answer_hub(question_str))




