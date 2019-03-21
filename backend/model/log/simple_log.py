# -*- coding: utf-8 -*-
# File: similar_question_bot.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-21

import time
class simpleLog():

    @classmethod
    def log_something(cls, log_str):
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        with open('../../log/simple_log.txt', 'a', encoding='utf8') as out_file:
            out_file.write(now_time+'\t'+log_str+'\n')



