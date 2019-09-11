class Solution:
    def PrintMinNumber(self, numbers):
        def compare(x, y):
            if '{}{}'.format(x,y) > '{}{}'.format(y,x):
                return 1
            return -1

        numbers = [str(num) for num in numbers]
        return ''.join(sorted(numbers, cmp=compare))

