class Solution:
    def Sum_Solution(self, n):
        ans = n
        return ans and ans + self.Sum_Solution(n-1)
