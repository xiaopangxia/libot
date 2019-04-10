# -*- coding: utf-8 -*-
# File: rdf_bot_multiwheel.py
# Author: LG
# CreateDate: 19-04-09
import os
import sys
# 模块路径引用统一回退到Libbot目录下
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)

from model.config.base_config import GraphBaseConfig
import model.config.multiwheel_manage as multiwheelUnit
from model.kb_prepare.rdf_prepare import rdfPrepare
import time
import datetime
import numpy as np
class rdfBotMul():
    """
    对应问题模式在知识图谱中查找答案
    目前包括读者卡办理
    """
    @classmethod
    def task_response(cls, task, entity_dict, question_str, graph):
        """
        响应hub指派的回答任务，也就是对graphQA类的问题分intent处理
        :param task:
        :return:
        """
        answer = "GraphQA 什么也没说！"
        if task == 'multiwheeltask_business_readerCard_00':
            answer = cls.answer_business_readerCard_00(entity_dict, graph)
        elif task == 'multiwheeltask_business_readerCard_yes':
            answer = cls.answer_business_readerCard_yes(entity_dict, graph)
        elif task == 'multiwheeltask_business_readerCard_no':
            answer = cls.answer_business_readerCard_no(entity_dict, graph)
        return answer

    @classmethod
    def answer_business_readerCard_00(cls, entity_dict, graph):
        respons_str=""
        if (len(rdfPrepare.rdf_query_propertiy("办理读书卡", "pro_step1", graph)) != 0):
            respons_str += rdfPrepare.rdf_query_propertiy("办理读书卡", "pro_step1", graph)[0]
            if multiwheelUnit.get_value('business') == None:
                multiwheelUnit.set_value('business', "办理读书卡")
            if multiwheelUnit.get_value('step') == None:
                multiwheelUnit.set_value('step', "_step1")
            return respons_str
        else:
            return None

    @classmethod
    def answer_business_readerCard_yes(cls, entity_dict, graph):
        if multiwheelUnit.get_value('business')=="办理读书卡":
            if multiwheelUnit.get_value('step')!=None:
                arr = multiwheelUnit.get_value('step').split('_')
                step=arr[len(arr) - 1]
                if (len(rdfPrepare.rdf_query_propertiy("办理读书卡", "pro_"+step+"_yes", graph)) != 0):
                    step_ans =rdfPrepare.rdf_query_propertiy("办理读书卡", "pro_"+step+"_yes", graph)[0]
                    respons_str=rdfPrepare.rdf_query_propertiy("办理读书卡", "pro_"+step_ans, graph)[0]
                    multiwheelUnit.set_value('step',multiwheelUnit.get_value('step')+"_"+step_ans)
                    return respons_str
        else:
            return None
    @classmethod
    def answer_business_readerCard_no(cls, entity_dict, graph):
        if multiwheelUnit.get_value('business')=="办理读书卡":
            if multiwheelUnit.get_value('step')!=None:
                arr = multiwheelUnit.get_value('step').split('_')
                step=arr[len(arr) - 1]
                if (len(rdfPrepare.rdf_query_propertiy("办理读书卡", "pro_"+step+"_no", graph)) != 0):
                    step_ans =rdfPrepare.rdf_query_propertiy("办理读书卡", "pro_"+step+"_no", graph)[0]
                    respons_str=rdfPrepare.rdf_query_propertiy("办理读书卡", "pro_"+step_ans, graph)[0]
                    multiwheelUnit.set_value('step',multiwheelUnit.get_value('step')+"_"+step_ans)
                    return respons_str
        else:
            return None