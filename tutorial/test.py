# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
    gsliu 2017-03-09
    
"""
import json

a = {'少吃点':' 啊','安抚':1,'大叔':'发'}
# a = json.dumps(a).decode('unicode-escape')
b = [a]
b = json.dumps(b).decode('unicode-escape')
print b
with open('data.txt', 'a') as f:
    f.write(b.encode('utf-8'))
