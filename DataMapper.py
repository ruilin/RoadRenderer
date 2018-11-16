#!/usr/bin/python
# -*- coding:UTF-8 -*-
import math


class Mapper:
    __canvasX = 0
    __canvasY = 0
    __canvasW = 0
    __canvasH = 0
    __rotateDegree = 0.0
    __scale = 0.0

    def __init__(self, canvas_w, canvas_h):
        self.__canvasW = canvas_w
        self.__canvasH = canvas_h
        self.__canvasX = canvas_w / 2
        self.__canvasY = canvas_h / 2

    def mapping(self, path):
        # base_point = [(path[0][0] + path[len(path) - 1][0]) / 2, (path[0][1] + path[len(path) - 1][1]) / 2]
        count_x = 0.0
        count_y = 0.0
        for i in range(len(path)):
            count_x += path[i][0]
            count_y += path[i][1]
        base_point = [count_x / len(path), count_y / len(path)]

        self.__rotateDegree = Mapper.calc_rotate(path[0], path[1])

        # 计算缩放级别
        # self.__scale = 1.06
        self.__scale += self.__calc_scale(path, base_point)
        
        # 数据转换
        result = self.__process_single_point(path, base_point)

        return result

    def __process_point_offset(self, data, base_point, degree, scale):
        diff_x = (data[0] - base_point[0]) * 10000.0
        diff_y = (data[1] - base_point[1]) * 10000.0

        x = diff_x
        y = diff_y
        if degree != 0:
            radians = math.radians(90 - degree)
            sin = Mapper.round(math.cos(radians))
            cos = Mapper.round(math.sin(radians))
            x = ((diff_x * cos) - (diff_y * sin))
            y = ((diff_x * sin) + (diff_y * cos))
        y = -y
        x *= scale
        y *= scale
        return [x, y]

    def __process_single_point(self, data, base_point):
        new_data = []
        for i in range(len(data)):
            offset = self.__process_point_offset(data[i], base_point, self.__rotateDegree, self.__scale)
            x = offset[0]
            y = offset[1]
            x += self.__canvasX
            y += self.__canvasY
            new_data.append([x, y])

        return new_data

    def __calc_scale(self, path, base_point):
        # 计算缩放级别
        # edge_point = self.__process_point_offset(path[0], base_point, self.__rotateDegree)

        left = [0, 0]
        right = [0, 0]
        top = [0, 0]
        bottom = [0, 0]
        for i in range(len(path)):
            point = self.__process_point_offset(path[i], base_point, self.__rotateDegree, 1)
            if point[0] < left[0]:
                left = point
            if point[0] > right[0]:
                right = point
            if point[1] < top[1]:
                top = point
            if point[1] > bottom[1]:
                bottom = point

        if abs(left[0]) > abs(right[0]):
            is_left = True
            edge_x = abs(left[0])
        else:
            is_left = False
            edge_x = abs(right[0])

        if abs(top[1]) > abs(bottom[1]):
            is_top = True
            edge_y = abs(top[1])
        else:
            is_top = False
            edge_y = abs(bottom[1])

        if (edge_x / self.__canvasW) > (edge_y / self.__canvasH):
            if is_left:
                edge_point = left
            else:
                edge_point = right
        else:
            if is_top:
                edge_point = top
            else:
                edge_point = bottom

        diff_x = abs(edge_point[0])
        diff_y = abs(edge_point[1])
        mul_x = 0
        if diff_x != 0:
            mul_x = abs((self.__canvasX - diff_x) / diff_x)
        mul_y = 0
        if diff_y != 0:
            mul_y = abs((self.__canvasY - diff_y) / diff_y)
        return mul_x if (mul_x < mul_y) else mul_y

    @staticmethod
    def calc_rotate(s_point, e_point):
        atan = math.atan2((e_point[0] - s_point[0]), (e_point[1] - s_point[1]))
        deg = math.degrees(atan)
        return deg

    @staticmethod
    def round(value):
        return round(value * 1000000) / 1000000
