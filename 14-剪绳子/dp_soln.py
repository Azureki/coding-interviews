class Solution:
    def cutRope(self, number):
        if number < 4:
            return number - 1
        dp = list(range(number + 1))
        for i in range(4, number + 1):
            max_prod = 0
            for j in range(1, i // 2 + 1):
                prod = dp[j] * dp[i - j]
                if prod > max_prod:
                    max_prod = prod
            dp[i] = max_prod

        return dp[number]
