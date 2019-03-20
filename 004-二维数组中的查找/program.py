# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        width = len(array[0])
        height = len(array)
        row = 0
        col = width - 1
        if col < 0:
            return False

        while True:
            if target < array[row][col]:
                col -= 1
                if col == -1:
                    break
            elif target > array[row][col]:
                row += 1
                if row == height:
                    break
            else:
                return True
        return False
