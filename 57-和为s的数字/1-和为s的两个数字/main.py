import sys


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if not array:
            return []
        product = sys.maxsize
        num1 = num2 = 0
        small, big = 0, len(array) - 1
        while small != big:
            if array[small] + array[big] < tsum:
                small += 1
            elif array[small] + array[big] > tsum:
                big -= 1
            else:
                # print("yes", small, big)
                tem = array[small] * array[big]
                if tem < product:
                    num1, num2 = array[small], array[big]
                    product = tem
                small += 1
            # print(small, big)
        return num1, num2 if num1 != num2 else []


# array, tsum = [1, 2, 4, 7, 11, 15], 15
array, tsum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],21
array, tsum = [], 0
res = Solution().FindNumbersWithSum(array, tsum)
print(res)
