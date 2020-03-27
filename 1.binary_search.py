# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   Algorithm Diagram 
File Name：     1.binary_sorting
Description :   二分查找
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020/2/21 14:19
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020/2/21:
-------------------------------------------------
"""


def binary_search(list, item):  # list数据包，目标元素item 注意写函数开头不能为数字，必须带冒号：
    low = 0  # 低索引
    high = len(list) - 1  # low和high用于跟踪要在其中查找的列表部分 | 高索引为 len - 1（初始低索引为0）
    while low <= high:  # 只要范围没有缩小到之包含一个元素
        # mid = (low +high)
        mid = int((low + high) / 2)  # 就检查中间的元素 （书中错误，已更正）
        guess = list[mid]   # 获取中间元素
        if guess == item:  # 找到了元素 guess 即为 目标元素 item 则返回 索引 mid
            return mid
        if guess > item:  # 猜的数字大了 将高索引更改为 mid - 1
            high = mid - 1
        else:  # 猜的数字小了 将低索引更改为 low + 1
            low = mid + 1
    return None  # 没有指定的元素


# 来测试一下！
my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))  # => 1 别忘了索引从0开始，第二个位置的索引为1
print(binary_search(my_list, -1))  # => None 在python中，None表示空，它意味着没有找到指定的元素
