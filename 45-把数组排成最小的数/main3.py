from functools import cmp_to_key


class Solution:
    def PrintMinNumber(self, numbers):
        def compare(x, y):
            if f'{x}{y}' > f'{y}{x}':
                return 1
            return -1

        numbers = [str(num) for num in numbers]
        return ''.join(sorted(numbers, key=cmp_to_key(compare)))


lst = [3, 32, 321]
print(Solution().PrintMinNumber(lst))
