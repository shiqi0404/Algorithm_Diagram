# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   Algorithm Diagram 
File Name：     2.choose_sorting
Description :   选择排序
                将数组元素按从小到大的顺序排列
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020/2/24 14:02
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020/2/24:
-------------------------------------------------
"""
# 用来找出数组中最小元素的函数
def findSmallest(arr):
    smallest = arr[0]   # 存储最小的值
    smallest_index = 0  # 存储最小元素的索引
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
# 选择排序算法
def selectionSort(arr): # 对数组进行排序
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)    # 找出数组中最小的元素，并将其加入到新数组中
        newArr.append(arr.pop(smallest))
    return newArr
# 测试
print selectionSort([5,3,6,2,10])