# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   Algorithm Diagram 
File Name：     7.Dijkstra_Algorithm
Description :   狄克斯特拉算法
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-04-02 18:39
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-04-02:
-------------------------------------------------
"""
graph = {}                  # 存储每个节点邻居
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
# 因此graph["start"]是一个散列表，要获取起点的所有邻居可用print
print graph["start"].keys()

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}           # 终点没有任何邻居

infinity = float("inf")     # python中表示无穷大
costs = {}                  # 存储每个节点开销
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents = {}                # 存储每个节点父节点
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = "None"

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:				                            # 遍历所有的节点
        cost = costs[node]
        if cost < lowest_cost and node not in processed:        # 如果当前节点的开销更低且未处理过
            lowest_cost = cost 		                            # 就将其视为开销最低的节点
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)         # 在未处理得节点中找出开销最小得节点
while node is not None:				        # 在所有节点都被处理过后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():		        # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:	            # 如果经当前节点前往该邻居更近
            costs[n] = new_cost		        # 就更新该邻居的开销
            parents[n] = node		        # 同时将该邻居的父节点设置为当前节点
    processed.append(node)			        # 将当前节点标记为处理过
    node = find_lowest_cost_node(costs)	    # 找出接下来要处理的节点，并循环


