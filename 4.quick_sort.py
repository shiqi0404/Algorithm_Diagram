# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   Algorithm Diagram 
File Name：     quick_sort
Description :   
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-03-29 20:45
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-03-29:
-------------------------------------------------
"""
from time import sleep


def sum(arr):
	total = 0
	for x in arr:
		total += x
	return total


print sum([1, 2, 3])


def quicksort(array):
    if len(array) < 2:
        return array    # 基线条件：为空或只包含一个元素的数组是“有序”的
    else:
        pivot = array[0]    # 递归条件
        less = [i for i in array[1:] if i <= pivot]
        # 由所以小于基准值的元素组成的子数组
        greater = [i for i in array[1:] if i > pivot]
        # 由所以大于基准值的元素组成的子数组
    return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10,5,2,3]))
print(quicksort([10,5,2,3,11,15,12]))


def print_items(list):
    for item in list:
        print item


# from time import sleep # 为了规范，置顶了
def print_items2(list):
    for item in list:
        sleep(1)
        print item