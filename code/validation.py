# -*- coding: utf-8 -*-
from format import Format

format = Format()

class Validation(object):
    """输入验证模块"""
    def inputs(self,str):
        ##验证信息输入是否为空，若为空，重复提示内容。即原版的 input_request()##

        ##todo:过滤掉输入两侧的空格##
        
        content = input(str)
        while content == '':
            format.breakLine('-',50)
            content = input(str)
        return content

