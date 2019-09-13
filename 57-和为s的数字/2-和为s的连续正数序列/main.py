class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        res = []
        small, big, mid = 1, 2, (1 + tsum) // 2
        cur_sum = small + big
        while small < mid:
            if cur_sum > tsum:
                cur_sum -= small
                small += 1
                continue
            elif cur_sum == tsum:
                res.append(list(range(small, big + 1)))
            big += 1
            cur_sum += big
        return res


print(Solution().FindContinuousSequence(100))
