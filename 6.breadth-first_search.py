# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   Algorithm Diagram 
File Name：     6.breadth-first_search
Description :   广度优先搜索
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-04-01 20:12
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-04-01:
-------------------------------------------------
"""
from collections import deque
# 6.3
graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print graph

# 更换  ["anuj"]  和  ["claire"] 顺序
graph = dict()
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["anuj"] = []
graph["claire"] = ["thom", "jonny"]
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print graph

# 6.5
# from collections import deque     # deque函数创建一个双端队列

search_queue = deque()          # deque函数创建一个双端队列
search_queue += graph["you"]


def person_is_seller(name):     # 这个函数检查人的姓名是否以m结尾，如果是，他就是芒果销售商。
    return name[-1] == 'm'


while search_queue:             # 列表不为空
    person = search_queue.popleft()     # popleft返回队列左边的第一个
    if person_is_seller(person):        # 进行判断，用定义的函数
        print(person + " is a mango seller!")
    else:
        search_queue += graph[person]   # 不是的话继续递归

# Output: thom is a mango seller!

def search(name):
    search_queue = deque()          # 创建一个队列
    search_queue += graph[name]     # 将你的邻居都加入到这个搜索队列中 graph["you"]是一个数组
    searched = []                   # 这个数组用于记录检查过的人
    while search_queue:             # 只要队列不为空
        person = search_queue.popleft()                 # 就取出其中的第一个人
        if not person in searched:                      # 仅当这个人没检查过时才检查
            if person_is_seller(person):                # 检查这个人是否是芒果销售商
                print person + " is a mango seller!"    # 是芒果销售商
                return True
            else:
                search_queue += graph[person]   # 不是芒果销售商。将这个人的朋友都加入搜索队列
                searched.append(person)         # 将这个人标记为检查过
    return False                                # 如果到达了这里，就说明队列中没人是芒果销售商


search("you")   # Output: thom is a mango seller!
