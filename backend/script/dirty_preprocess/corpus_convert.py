# -*- coding: utf-8 -*-
# File: corpus_convert.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-07

import json

def xiaohuangji2chatterbot():
    """
    格式转化，将小黄鸡语料转成chatterbot训练语料
    :return:
    """
    with open('xiaohuangji.conv', 'r', encoding='utf8') as in_file:
         seg_list = in_file.read().split('E')
         dialog_list = []
         for seg in seg_list:
             try:
                 seg = seg.strip()
                 if len(seg)>4:
                     que = seg.split('\n')[0].strip('M').strip()
                     ans = seg.split('\n')[1].strip('M').strip()
                     dialog_list.append([que, ans])
             except Exception as e:
                 print(seg)
         chatterbot_corpus = {"conversations": dialog_list}
         out_file = open('xiaohuangji_chatterbot_corpus.json', 'a', encoding='utf8')
         json.dump(chatterbot_corpus, out_file)

if __name__=='__main__':
    xiaohuangji2chatterbot()

