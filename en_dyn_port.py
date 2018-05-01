#! /usr/bin/env python
# -*- coding: utf-8 -*-
import readjson
import writejson
from utils import is_number


#主要程序部分
print ("是否使能动态端口(y/n)")
newport=raw_input()
if newport == 'y':
    writejson.EnDynPort(1)
elif newport == 'n':
    writejson.EnDynPort(0)
else:
    print ("输入错误，请检查是否为数字")

