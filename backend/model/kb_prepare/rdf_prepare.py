# -*- coding: utf-8 -*-
# File: rdf_prepare.py
# Author: Hualong Zhang <nankaizhl@gmail.com>
# CreateDate: 19-03-10
import os
import sys
# 模块路径引用统一回退到Libbot目录下
project_path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
sys.path.append(project_path)

from rdflib import URIRef, Literal

class rdfPrepare():
    @classmethod
    def create_rdf_from_triples(cls, triple_file, graph_file):
        """
        从三元组文件构建图，存成RDF
        :param triple_file:
        :param graph_file:
        :return:
        """
        pass






