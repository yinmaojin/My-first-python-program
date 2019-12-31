# Users/尹茂金/PycharmProjects
# !-*- coding:utf-8 -*-
# !@time:2019/12/10,8:50
# !@Author: 尹茂金
# !@File:实验十一.py
class Man(object):
    def __init__(self, name, age, weigh, height):
        self.name = name
        self.age = age
        self.weigh = weigh
        self.height = height

    def work_time(self, time):
        if 8 <= time <= 12:
            self.weigh -= 2
        elif time > 12:
            self.weigh -= 5

    def judge_body(self):
        if self.height - 105 == self.weigh:
            return "身材标准"
        elif self.height - 105 > self.weigh:
            return "身材偏瘦"
        elif self.height - 105 < self.weigh:
            return "身材偏胖"


p1 = Man("Chen", 29, 130, 170)
p1.work_time(13)
print(p1.judge_body())
