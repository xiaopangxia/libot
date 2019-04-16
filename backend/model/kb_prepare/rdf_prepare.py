#coding:utf-8
#Author: Liu liting <nkliuliting826@mail.nankai.edu.cn>
# CreateDate: 19-03-29

import rdflib
import xlrd
from rdflib import Literal
from rdflib.namespace import RDF
RDF.type = rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#type')


class rdfPrepare():

    @classmethod
    def excel_to_RDF(cls, triple_file, graph_file):

        """
        从三元组表格文件构建数据对象，存成rdf
        :param triple_file:
        :param graph_file:
        :return:
        """

        # 打开文件
        entities = xlrd.open_workbook(triple_file)
        g = rdflib.Graph()

        key = dict()
        col_names = dict()
        num_properties = dict()
        num_relations = dict()

        sheetnames = entities.sheet_names()

        # 获取所有给定名字的sheet
        entity = dict()
        for num, sheetname in enumerate(sheetnames):
            entity[sheetname] = entities.sheet_by_name(sheetname)
            # namespace[sheetname] = Namespace('http://www.libot.org/'+sheetname+'/')
            sheet_name = rdflib.URIRef('http://www.libot.org/' + sheetname)
            print(sheet_name)
            col_names[sheetname] = entity[sheetname].row_values(0)
            num_properties[num] = 0
            num_relations[num] = 0

            for col_name in col_names[sheetname]:
                if col_name.startswith("pro"):
                    num_properties[num] += 1
                elif col_name.startswith("rel"):
                    num_relations[num] += 1
            print(sheetname + " " + str(num_properties[num]) + " " + str(num_relations[num]))

            colvalue = dict()
            property = dict()

            # 定义关系和属性名
            for i in range(1, num_properties[num] + 1):
                # 获取属性
                property[col_names[sheetname][i]] = rdflib.URIRef(
                    'http://www.libot.org/' + str(col_names[sheetname][i]))
                colvalue[col_names[sheetname][i]] = entity[sheetname].col_values(i)
            # print(property.keys())
            # 主键名字
            # keyname = col_names[0]

            keyvalues = entity[sheetname].col_values(0)
            # print(len(entity.col_values(0)))
            for j in range(1, len(entity[sheetname].col_values(0))):
                # 定义实体URI
                key[keyvalues[j]] = rdflib.URIRef(
                    'http://www.libot.org/' + keyvalues[j].replace(' ', '').replace('\n', ''))
                g.add((key[keyvalues[j]], RDF.type, sheet_name))
                # 构建实体-属性值三元组
                for m in range(1, num_properties[num] + 1):
                    if (colvalue[col_names[sheetname][m]][j]):
                        g.add((key[keyvalues[j]], property[col_names[sheetname][m]],
                               Literal(str(colvalue[col_names[sheetname][m]][j]).replace(' ', '').replace('\n', ''))))

        # 构建实体-实体三元组
        relation = dict()
        for num, sheetname in enumerate(sheetnames):
            for k in range(num_properties[num] + 1, num_properties[num] + num_relations[num] + 1):
                # 获取关系
                print(k)
                print(col_names[sheetname][k])
                relation[col_names[sheetname][k]] = rdflib.URIRef(
                    'http://www.libot.org/' + str(col_names[sheetname][k]))
            for j in range(1, len(entity[sheetname].col_values(0))):
                for r in range(num_properties[num] + 1, num_relations[num] + num_properties[num] + 1):
                    second_entity_list = entity[sheetname].col_values(r)[j].strip().split('，')
                    for sec_entity in second_entity_list:
                        if sec_entity in key.keys():
                            g.add((key[entity[sheetname].col_values(0)[j]], relation[col_names[sheetname][r]],
                                   key[sec_entity]))

        g.serialize(graph_file)

    @classmethod
    def load_graph(cls):
        g = rdflib.Graph()
        g.parse("../../resource/libot.rdf", format="xml")
        return g

    @classmethod
    def load_navi_graph(cls):
        navi_g = rdflib.Graph()
        navi_g.parse("../../resource/navigation2.rdf", format="xml")
        return navi_g

    @classmethod
    def rdf_query_propertiy(cls,entity, intension, g):

        q = "select?part where {<http://www.libot.org/" + entity + "> <http://www.libot.org/" + intension + "> ?part}"

        x = g.query(q)
        t = list(x)
        #print(t)
        part_list = []
        for i in range(len(t)):
            part_list.append(t[i][0])
            # print(t[i][0])
        return part_list

    @classmethod
    def rdf_query_navi_propertiy_dis(cls, entity, intension, g):

        q = "select?part where {<http://www.libot.org/" + entity + "> <http://www.libot.org/" + intension + "> ?part}"
        # print(q)
        x = g.query(q)
        t = list(x)
        #t = list(x)
        #print('？',t)
        vlist = t[0][0].strip().split('米，')
        del vlist[len(vlist)-1]
        #print(vlist)

        return vlist

    @classmethod
    def rdf_query_navi_propertiy(cls, entity, intension, g):

        q = "select?part where {<http://www.libot.org/" + entity + "> <http://www.libot.org/" + intension + "> ?part}"
        #print(q)
        # print(q)
        x = g.query(q)
        t = list(x)
        # t = list(x)
        #print('？',t)
        #print(t)
        vlist = t[0][0].strip().split('，')


        return vlist

    @classmethod
    def rdf_query_navi_propertiy_pic(cls, entity, intension, g):

        q = "select?part where {<http://www.libot.org/" + entity + "> <http://www.libot.org/" + intension + "> ?part}"
        # print(q)
        # print(q)
        x = g.query(q)
        t = list(x)
        # t = list(x)
        #print('？',t)
        # print(t)
        vlist = t[0][0].strip().split('；')
        #print(vlist)

        return vlist



    @classmethod
    def rdf_query_relation(cls, entity, intension, g):

        q = "select?part where {<http://www.libot.org/" + entity + "> <http://www.libot.org/" + intension + "> ?part}"
        #print(q)
        x = g.query(q)
        t = list(x)
        #print(t)
        part_list = []
        #print(t[0][0])

        for i in range(len(t)):
            part_list.append(t[i][0].split('/')[3])
        #print(part_list)

        return part_list

    @classmethod
    def rdf_navi_query_relation(cls, entity, intension, g):

        q = "select?part where {<http://www.libot.org/" + entity + "> <http://www.libot.org/" + intension + "> ?part}"
        # print(q)
        x = g.query(q)
        t = list(x)
        #print(t)
        part_list = []


        for i in range(len(t)):
            part_list.append(str(t[i][0]))


        return part_list

    @classmethod
    def rdf_query_entity_list(cls, type, g):

        q = "select?part where {?part <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.libot.org/" + type + ">}"

        # print(q)
        x = g.query(q)
        t = list(x)
        #print(t)
        entity_list = []
        for i in range(len(t)):
            # print(t[i][0])
            entity_list.append(t[i][0])
        #print(entity_list[1])
        return entity_list

    @classmethod
    def rdf_query_varientnames(cls, type, g):
        entity_list = rdfPrepare.rdf_query_entity_list(type,g)
        #print(entity_list)
        varient_list = dict()
        for enity in entity_list:
            q = "select?part where {<"+str(enity)+"> <http://www.libot.org/pro_variant_name> ?part}"

            x = g.query(q)
            t = list(x)
            #print(t)

            #print(t[0])
            vlist = t[0][0].strip().split('，')
            #print(str(enity).split('/'))
            enity_name = str(enity).split('/')[3]
            varient_list[enity_name] = []
            varient_list[enity_name].extend(vlist)

        return varient_list
        #return None

    @classmethod
    def rdf_query_allvarient(cls, g):
        """
        目前三个表
        :param g:
        :return:
        """
        q = "select?part?var where {?part <http://www.libot.org/pro_variant_name> ?var}"
        x = g.query(q)
        t = list(x)
        var_list = []
        for i in range(len(t)):
            # print(t[i][1])
            var_list += t[i][1].split('，')
            # print(var_list)
        return var_list


    @classmethod
    def rdf_query_name(cls, varname, type, g):
        name_list = []
        varname_dict_list = cls.rdf_query_varientnames(type, g)
        varnames = list(varname_dict_list.keys())
        varvalue = list(varname_dict_list.values())
        for num, var_list in enumerate(varvalue):
            # print(var_list)
            if varname in var_list:
                name_list.append(varnames[num])
        return name_list


    @classmethod
    def rdf_queryreverse_relation(cls, relation, intension, type, g):
        q = "select?entity where " \
            "{?entity <http://www.libot.org/" + intension + "> <http://www.libot.org/"+ relation +"> ." \
              "?entity <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.libot.org/"+type+">}"
        #print(q)
        x = g.query(q)
        t = list(x)
        #print(t)
        entity_list = []
        for i in range(len(t)):
            entity_list.append(t[i][0].split('/')[3])
        # print(entity_list)
        return entity_list

    @classmethod
    def rdf_navi_query_reverse_relation(cls, relation, intension, type, g):
        q = "select?entity where " \
            "{?entity <http://www.libot.org/" + intension + "/"+ relation + "> ." \
            "?entity <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.libot.org/" + type + ">}"
        #print(q)

        x = g.query(q)
        t = list(x)
        #print(t)
        entity_list = []
        for i in range(len(t)):
            entity_list.append(str(t[i][0]))

        return entity_list

    @classmethod
    def rdf_query_count(cls, enity, g):

        q = "select?part where {<http://www.libot.org/" + str(enity) + "> <http://www.libot.org/pro_count> ?part}"
        x = g.query(q)
        t = list(x)
        vlist = t[0][0].strip().split('，')

        return vlist

    @classmethod
    def test(cls, g):

        q = "select?part where {<http://www.libot.org/中文_普通图书（含民国平装书）> <http://www.libot.org/pro_count> ?part}"
        x = g.query(q)
        t = list(x)
        vlist = t[0][0].strip().split('，')
        #print(vlist)
        return t





if __name__ == '__main__':
    navi_g = rdfPrepare.load_navi_graph()
    g = rdfPrepare.load_graph()
    #总馆北区_F1_少年儿童馆_1
    #a = rdfPrepare.rdf_query_varientnames('room', navi_g)

    #rdfPrepare.excel_to_RDF(r'../../resource/one.xlsx',"../../resource/one.rdf")
    #g = rdfPrepare.load_graph()
    #rdfPrepare.rdf_query_varientnames('room',g)
    #a=rdfPrepare.rdf_query_count('中文_普通图书（含民国平装书）',g)
    #print(a)
    #c = rdfPrepare.rdf_navi_query_reverse_relation('总馆南区','rel_part_of_room','room',navi_g)
    #a = rdfPrepare.rdf_query_relation('总馆北区_F2_标志位B_2','rel_part_of_room',navi_g)
    pos_near_machine = rdfPrepare.rdf_query_navi_propertiy('总馆北区_F2_标志位D_2', 'pro_des_dis', navi_g)
    #b = rdfPrepare.rdf_queryreverse_relation('总馆南区', 'rel_part_of_room', 'room',g)
    #print(pos_near_machine)
    # var = ["亲子区"]
    # rdfPrepare.rdf_query_name("小儿馆","room",g)
    #rdfPrepare.rdf_queryreverse_relation('台港澳文献阅览室','rel_part_of_room','resource',g)
    # print(rdfPrepare.rdf_query_propertiy("中文期刊区",'pro_open_day',g))
    # rdfPrepare.rdf_queryreverse_propertiy('周一至周五（周六、周日不开放）','pro_open_day',g)






