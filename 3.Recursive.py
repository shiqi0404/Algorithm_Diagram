# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name:   Algorithm Diagram 
File Name：     3.Recursive
Description :   递归、栈、调用栈、递归调用栈
Author :        Steven.zou
E-mail:         zoushiqi0404@gmail.com
Date：          2020-03-28 10:59
Software:       PyCharm
-------------------------------------------------
 Change Activity:
                   2020-03-28:
-------------------------------------------------
"""


# 3.1 递归
# Solution 1：(while 循环: 只要盒子堆不空，就从中取一个盒子，并在其中仔细查找。)
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print "found the key!"


#  Solution 2：(递归, 函数调用自身)
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)  # 递归
        elif item.is_a_key():
            print "found the key!"


# 3.2 基线条件和递归条件
# objective: 3...2...1
def countdown(i):     # 死循环
    print i
    countdown(i-1)


# 加入基线条件改进
def countdown(i):
    print i
    if i <= 0:  # 基线条件
        return
    else:       # 递归条件
        countdown(i-1)


# 3.3 栈
# 3.3.1 调用栈
def greet(name):    # 这个函数问候用户，再调用另外两个函数。
    print "hello," + name + "!"
    greet2(name)
    print "getting ready to say bye ..."
    bye()


def greet2(name):
    print "how are you, " + name + "?"


def bye():
    print "ok bye!"


# 3.3.1 递归调用栈
def fact(x):
    if x == 1:
        return 1
    else:
        x * fact(x-1)


if __name__ == '__main__':
    countdown(100)      # 3.2 基线条件
    greet("Steven")     # 3.3.1 调用栈
    fact(5)             # 3.3.2 递归调用栈