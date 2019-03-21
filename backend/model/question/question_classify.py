# -*- coding: utf-8 -*-
# File: question_classify.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-09
import os
import sys
# 模块路径引用统一回退到Libbot目录下
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)


from model.data_utill.data_utill import DataUtill
from model.question.dict_match import DictMatch


class QuestionClassifier():
    """
    问题分类器，包括问题类型和意图
    """

    @classmethod
    def robot_classify_keywords(cls, question_str):
        """
        根据关键词与字典匹配对问题分类，并指派具体问答机器人
        不同方案机器人包括
        graph_QA
        template_QA
        reading_QA
        open_chat
        :return:
        """
        # graph_QA目前处理:时间,位置,联系方式
        time_kw_matched = DictMatch.dict_match(question_str, '../../resource/time_keywords.txt')
        position_kw_matched = DictMatch.dict_match(question_str, '../../resource/position_keywords.txt')
        contact_kw_matched = DictMatch.dict_match(question_str, '../../resource/contact_keywords.txt')
        room_matched = DictMatch.room_dict_match(question_str)
        resource_matched = DictMatch.resource_dict_match(question_str)
        # building_mached = DictMatch.building_dict_match(question_str)

        task_define_list = []   # 任务指派结果列表
        # transfer to graph QA
        if len(time_kw_matched) > 0 and len(resource_matched) > 0:
            task_define_list.append({'robot': 'graph_QA', 'intent': 'res_time', 'res_entity': resource_matched, 'question': question_str})
            # return {'robot': 'graph_QA', 'intent': 'res_time', 'res_entity': resource_matched, 'question': question_str}
        elif len(time_kw_matched) > 0 and len(room_matched) > 0:
            task_define_list.append({'robot': 'graph_QA', 'intent': 'room_time', 'room_entity': room_matched, 'question': question_str})
            # return {'robot': 'graph_QA', 'intent': 'room_time', 'room_entity': room_matched, 'question': question_str}
        elif len(contact_kw_matched) > 0 and len(room_matched) > 0:
            task_define_list.append({'robot': 'graph_QA', 'intent': 'room_contact', 'room_entity': room_matched, 'question': question_str})
            # return {'robot': 'graph_QA', 'intent': 'room_contact', 'room_entity': room_matched, 'question': question_str}
        elif len(position_kw_matched) > 0 and len(room_matched) > 0:
            task_define_list.append({'robot': 'graph_QA', 'intent': 'room_pos', 'room_entity': room_matched, 'question': question_str})
            # return {'robot': 'graph_QA', 'intent': 'room_pos', 'room_entity': room_matched, 'question': question_str}
        elif len(position_kw_matched) > 0 and len(resource_matched) > 0:
            task_define_list.append({'robot': 'graph_QA', 'intent': 'res_pos', 'res_entity': resource_matched, 'question': question_str})
            # return {'robot': 'graph_QA', 'intent': 'res_pos', 'res_entity': resource_matched, 'question': question_str}
        elif len(resource_matched) > 0 and len(room_matched) > 0:
            task_define_list.append({'robot': 'graph_QA', 'intent': 'res_room', 'res_entity': resource_matched, 'room_entity': room_matched, 'question': question_str})
            # return {'robot': 'graph_QA', 'intent': 'res_room', 'res_entity': resource_matched, 'room_entity': room_matched, 'question': question_str}


        # transfer to template QA
        banzheng_match_res = DictMatch.question_match_edit_dist(question_str, '../../resource/pair_for_banzheng.txt')
        jieyue_match_res = DictMatch.question_match_edit_dist(question_str, '../../resource/pair_for_jieyue.txt')
        if banzheng_match_res is not None:
            task_define_list.append({'robot': 'template_QA', 'intent': 'banzheng', 'qa_pair': banzheng_match_res[0][1], 'question': question_str})
            # return {'robot': 'template_QA', 'intent': 'banzheng', 'qa_pair': banzheng_match_res, 'question': question_str}
        elif jieyue_match_res is not None:
            task_define_list.append({'robot': 'template_QA', 'intent': 'jieyue', 'qa_pair': jieyue_match_res[0][1], 'question': question_str})
            # return {'robot': 'template_QA', 'intent': 'jieyue', 'qa_pair': jieyue_match_res, 'question': question_str}


        # transfer to reading QA
        # Xiaofei 在探索，目前采用问题库编辑距离代替
        reading_match_res = DictMatch.question_match_edit_dist(question_str, '../../resource/pair_for_reading_qa.txt')
        if reading_match_res is not None:
            task_define_list.append({'robot': 'search_QA', 'intent': 'rand', 'qa_pair': reading_match_res[0][1], 'question': question_str})
            # return {'robot': 'search_QA', 'intent': 'rand', 'qa_pair': reading_match_res, 'question': question_str}

        # transfer to open_chat
        # 目前只实现了小黄鸡语料的chatterbot
        task_define_list.append({'robot': 'open_chat', 'intent': 'chatterbot', 'question': question_str})
        # return {'robot': 'open_chat', 'intent': 'chatterbot', 'question':question_str}

        return task_define_list




if __name__ == '__main__':
    task_define_list = QuestionClassifier.robot_classify_keywords('办证处在哪')
    for task_define in task_define_list:
        print(task_define)

