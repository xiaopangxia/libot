# -*- coding: utf-8 -*-
# File: base_config.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-10
import time
import datetime

GraphBaseConfig = {
    'now_day': time.strftime('%Y{y}%m{m}%d{d} {w}%w', time.localtime(time.time())).format(y='年', m='月', d='日', w='星期').replace('星期0', '星期日'),
    'now_buiding': '总馆北区',
    'now_floor': '总馆北区二层'

}





