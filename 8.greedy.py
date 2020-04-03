# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   Algorithm Diagram 
File Name：     8.greedy
Description :   贪婪算法
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-04-03 22:46
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-04-03:
-------------------------------------------------
"""

# 准备工作
# 首先，创建一个列表，其中包含要覆盖的州
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])	# 传入一个数组，转换为集合
# 使用集合来表示要覆盖的州，集合类似于列表，集合不能包含重复的元素，则假设有
arr = [1, 2, 2, 3, 3, 3]
set(arr)                    # 转换为集合

# 创建可供选择的广播台清单
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
final_stations = set()		# 创建一个集合存储最终选择的广播台

# 计算答案
# 正解可能有多个，需要遍历所有的广播台并从中选择覆盖了最多的未覆盖的广播台。
while states_needed:
    best_station = None			# 将这个覆盖了最多的未覆盖的广播台存储在best_station 中
    states_covered = set()		# 集合：包含该广播台覆盖的所有未覆盖的州
    for station, states in stations.items():		# 循环每个广播台，并确定它是否是最佳的广播台
        covered = states_needed & states            # 计算并集：两个集合合并
        if len(covered) > len(states_covered):		            # 计算交集
            best_station = station
            states_covered = covered
    states_needed -= states_covered			# 更新states_needed 由于该广播台覆盖了一些州，因此不用再覆盖这些州
    final_stations.add(best_station)		# 将best_station添加入最终的广播台列表中

print final_stations
