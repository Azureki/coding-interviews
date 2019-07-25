import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        return heapq.nsmallest(k, tinput) if k<=len(tinput) else []
