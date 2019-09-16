class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        numbers.sort()
        num_of_kings = 0
        num_of_gaps = 0
        for x in numbers:
            if x != 0:
                break
            num_of_kings += 1
        start = num_of_kings

        for i in range(start, len(numbers) - 1):
            if numbers[i + 1] == numbers[i]:
                return False
            num_of_gaps += numbers[i + 1] - numbers[i] - 1

        return num_of_gaps <= num_of_kings


numbers = [0,3,2,6,4]
res = Solution().IsContinuous(numbers)
print(res)
