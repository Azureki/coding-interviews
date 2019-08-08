class Solution:
    def FindGreatestSumOfSubArray(self, array):
        greatest_sum = float('-inf')
        cur_sum = 0
        for x in array:
            if cur_sum <= 0:
                cur_sum = x
            else:
                cur_sum += x
            if cur_sum > greatest_sum:
                greatest_sum = cur_sum
        return greatest_sum


if __name__ == '__main__':
    lst = [6, -3, -2, 7, -15, 1, 2, 2]
    # lst = [1,-2,3,10,-4,7,2,-5]
    res = Solution().FindGreatestSumOfSubArray(lst)
    print(res)
