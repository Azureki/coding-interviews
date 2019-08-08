class Solution:
    def FindGreatestSumOfSubArray(self, array):
        dp = [0]*len(array)
        for i, x in enumerate(array):
            dp[i] = x if i == 0 or dp[i-1] <= 0 else dp[i-1]+x
        return max(dp)


if __name__ == '__main__':
    lst = [6, -3, -2, 7, -15, 1, 2, 2]
    # lst = [1,-2,3,10,-4,7,2,-5]
    res = Solution().FindGreatestSumOfSubArray(lst)
    print(res)
