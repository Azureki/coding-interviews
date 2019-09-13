from functools import reduce
from operator import xor


class Solution:
    def FindNumsAppearOnce(self, array):
        def find_one(num):
            tem = 1
            for _ in range(32):
                if num & tem:
                    return tem
                tem <<= 1

        num = reduce(xor, array)
        mask = find_one(num)
        lst1 = []
        lst2 = []
        for x in array:
            if x & mask:
                lst1.append(x)
            else:
                lst2.append(x)
        return reduce(xor, lst1), reduce(xor, lst2)

