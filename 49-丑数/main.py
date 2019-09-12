class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        ugly = [0] * index
        ugly[0] = 1
        idx2 = idx3 = idx5 = 0
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5
        for i in range(1, index):
            ugly[i] = min(next_multiple_of_2, next_multiple_of_3,
                          next_multiple_of_5)
            if ugly[i] == next_multiple_of_2:
                idx2 += 1
                next_multiple_of_2 = ugly[idx2] * 2
            if ugly[i] == next_multiple_of_3:
                idx3 += 1
                next_multiple_of_3 = ugly[idx3] * 3
            if ugly[i] == next_multiple_of_5:
                idx5 += 1
                next_multiple_of_5 = ugly[idx5] * 5
        return ugly[-1]


print(Solution().GetUglyNumber_Solution(10))
