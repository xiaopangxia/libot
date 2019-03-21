# -*- coding: utf-8 -*-
# File: json_prepare.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-10

import json
class jsonPrepare():
    @classmethod
    def create_json_from_table_file(cls, triple_file, json_file):
        """
        从三元组表格文件构建数据对象，存成json
        :return:
        """
        record_list = []
        with open(triple_file, 'r', encoding='utf8') as in_file:
            col_name = []
            for line in in_file.readlines():
                if len(col_name) == 0:
                    col_name = line.strip().split('\t')
                else:
                    item_list = line.strip().split('\t')
                    record_dict = {}
                    for i in range(len(item_list)):
                        record_dict[col_name[i]] = item_list[i].strip('#')

                    record_list.append(record_dict)
        out_file = open(json_file, 'a', encoding='utf8')
        json.dump(record_list, out_file)
        return record_list

    @classmethod
    def load_room_json(cls):
        """
        加载馆室json
        :return:
        """
        in_file = open('../../resource/room_table.json', 'r', encoding='utf8')
        room_record_list = json.load(in_file)
        return room_record_list

    @classmethod
    def load_res_json(cls):
        """
        加载资源json
        :return:
        """
        in_file = open('../../resource/res_table.json', 'r', encoding='utf8')
        res_record_list = json.load(in_file)
        return res_record_list


if __name__ == '__main__':
    record_list = jsonPrepare.create_json_from_table_file('../../resource/room_table.txt', '../../resource/room_table.json')
    for record in record_list:
        print(record)
    record_list = jsonPrepare.create_json_from_table_file('../../resource/res_table.txt', '../../resource/res_table.json')
    for record in record_list:
        print(record)



