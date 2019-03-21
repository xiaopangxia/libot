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
from model.grapg_QA.json_bot import jsonBot
from model import aiml_cn



class GeneralHub():
    """
    总控程序版本1
    """
    def __init__(self):
        self._aiml_kernal = aiml_cn.Kernel()
        self._aiml_kernal.learn('../../resource/template.aiml')

    def question_answer_hub(self, question_str):
        """
        问答总控，基于aiml构建问题匹配器
        :param question_str:问句输入
        :return:
        """
        question_replaced, entity_dict = entityMatch.match_and_replace_all(question_str)
        aiml_respons = self._aiml_kernal.respond(question_replaced)
        if 'task_' in aiml_respons:
            graph_respons = jsonBot.task_response(aiml_respons, question_str, entity_dict)
            return graph_respons
        else:
            return aiml_respons



if __name__ == '__main__':
    # GeneralHub.question_answer_hub('办证处在哪里啊？')
    # GeneralHub.question_answer_hub('我找存包处')
    test_hub = GeneralHub()
    while True:
        question_str = input('User:')
        if question_str == 'exit':
            break
        else:
            print('Libot:', test_hub.question_answer_hub(question_str))




