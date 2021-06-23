# -*- coding: utf-8 -*-

import os
import cgi
import urllib
import typing

# if 'QUERY_STRING' in os.environ:
#     # query = cgi.parse_qs(os.environ['QUERY_STRING'])  # 廃止されてた
#     query = urllib.parse.parse_qs(os.environ['QUERY_STRING'])
# else:
#     query = {}

# a = int(query['a'][0])  # データaを整数として読み込む
# b = int(query['b'][0])  # データbを整数として読み込む
# c = a + b  # aとbの足し算を行う

# open("test.txt", "w", encoding="utf-8").write(f"answer is {c}\n")


sentence = typing.run()

# 出力
print("Content-Type:text/javascript")
print()
print("callback({'answer':'%s'});" % (str(sentence)))
