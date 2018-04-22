#! /usr/bin/env python
# -*- coding: utf-8 -*-
# change alter ID
import uuid
import readjson
import writejson
from utils import is_number

print ("当前AlterId为：%s") % str(readjson.ConfAlterId)
alterid = raw_input("请输入新的alterID: ")

if (is_number(alterid)):
    writejson.WriteAlterId(alterid)
else:
    print ("输入错误，请检查是否为数字")

