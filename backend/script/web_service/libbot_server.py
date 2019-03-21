# -*- coding: utf-8 -*-
# File: general_hub_1.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-09
import os
import sys
# 模块路径引用统一回退到Libbot目录下
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)


import tornado
import tornado.web
import tornado.ioloop
import tornado.escape
import json
from tornado.httpserver import HTTPServer
from model.robot_hub.general_hub_1 import GeneralHub
from model.search_QA.similar_question_bot import similarQuestionBot
from model.log.simple_log import simpleLog


graph_qa_hub = GeneralHub()
search_bot = similarQuestionBot()

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        target = self.get_argument("target")
        # print(self.request.body.decode('utf-8'))
        query_body = json.loads(self.request.body.decode('utf-8'))
        question_str = query_body['question']
        simpleLog.log_something('question:'+question_str)
        if target == 'graph_qa':
            graph_respons = graph_qa_hub.question_answer_hub(question_str)
            res_dict = {'graph_answer': graph_respons}
            res_json = json.dumps(res_dict)
            self.write(res_json)
            simpleLog.log_something('graph_answer:'+graph_respons)
        elif target == 'search_qa':
            answer_list = search_bot.answer_question(question_str)
            res_dict = {'search_answer': answer_list}
            res_json = json.dumps(res_dict)
            self.write(res_json)
            simpleLog.log_something('search_answer:' + str(answer_list))
        elif target == 'all':
            graph_respons = graph_qa_hub.question_answer_hub(question_str)
            answer_list = search_bot.answer_question(question_str)
            res_dict = {'graph_answer': graph_respons, 'search_answer': answer_list}
            res_json = json.dumps(res_dict)
            self.write(res_json)
            simpleLog.log_something('graph_answer:' + graph_respons)
            simpleLog.log_something('search_answer:' + str(answer_list))


    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')


application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()



