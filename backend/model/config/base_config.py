# -*- coding: utf-8 -*-
# File: base_config.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-10
import time
import datetime

GraphBaseConfig = {
    'now_day': time.strftime('%Y{y}%m{m}%d{d} {w}%w', time.localtime(time.time())).format(y='年', m='月', d='日', w='星期').replace('星期0', '星期日'),
    #'now_machine': '总馆北区_F3_标志位B_3'


    #'now_machine': '总馆北区_F2_大厅_2'
    'now_buiding': '总馆北区',
    'now_floor': '总馆北区二层',
    #'now_machine': '总馆北区_F2_大厅_2'
    #'now_machine': '总馆北区_F3_标志位A_3'
    #'now_machine': '总馆北区_F4_标志位A_4'
    #'now_machine': '总馆北区_F2_标志位A_2'
    #'now_machine': '总馆北区_F3_标志位B_3'

    #'now_machine': '总馆北区_F4_标志位B_4'
    #'now_machine': '总馆北区_F2_标志位B_2'
    #'now_machine': '总馆北区_F3_标志位C_3'
    #now_machine': '总馆北区_F4_标志位C_4'
    #'now_machine': '总馆北区_F2_标志位C_2'
    #'now_machine': '总馆北区_F3_标志位D_3'
    #'now_machine': '总馆北区_F4_标志位D_4'
    #'now_machine': '总馆北区_F2_标志位D_2'
    #'now_machine': '总馆北区_F1_标志位_1'
    #'now_machine': '总馆北区_F1_标志位_2'
    #'now_machine': '总馆北区_F1_标志位_3'
    #'now_machine': '总馆北区_F1_标志位_4'
    'now_machine': '总馆北区_F1_标志位_5'
}





