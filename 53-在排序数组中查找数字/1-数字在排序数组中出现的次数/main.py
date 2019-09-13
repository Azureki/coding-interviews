# from bisect import bisect_left


class Solution:
    def GetNumberOfK(self, data, k):
        left = bisect_left(data, k)
        if left == len(data) or data[left] != k:
            return 0
        right = bisect_left(data, k + 1, left + 1)
        return right - left


def bisect_left(nums, target, lo=0, hi=None):
    if hi is None:
        hi = len(nums)
    while lo < hi:
        mid = (lo + hi) / 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo
