# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   Algorithm Diagram 
File Name：     5.hash_table
Description :   散列表，最有用的基本数据结构之一。
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-03-31 9:45
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-03-31:
-------------------------------------------------
"""
# 5.1
book = dict()           # 散列表，在python中为字典，直接调用dict()

book["apple"] = 0.67    # 一个苹果的价格为67美分
book["milk"] = 1.49     # 牛奶的价格为1.49美元
book["avocado"] = 1.49

print book
print book["avocado"]   # 鳄梨的价格

# 5.2
# Case 1
phone_book = dict()     # 散列表
# phone_book = {}       # 与前面等效
phone_book["jenny"] = 8675309
phone_book["emergency"] = 911

print phone_book["jenny"]

voted = {}              # 创建散列表


# Case 2
def check_voter(name):
    if voted.get(name):         # 检查name在表中，返回let them vote!，否则返回kick them out!
        print "kick them out!"
    else:
        voted[name] = True
        print "let them vote!"


check_voter("tom")      # tom第一次投票
check_voter("mike")     # mike第一次投票
check_voter("mike")     # mike第二次投票会被拒绝


# Case 3
cache = {}


def get_page(url):
    if cache.get(url):
        return cache[url]   # 返回缓存的数据
    else:
        data = get_data_from_server(url)
        cache[url] = data   # 先将数据保存到缓存中
        return data