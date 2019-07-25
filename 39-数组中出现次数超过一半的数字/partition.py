class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        def check_res(tar):
            return sum(x == tar for x in numbers) > len(numbers) // 2
        left, right = 0, len(numbers) -1
        mid = (right - left) //2
        index = None
        while index != mid:
            index = partition(numbers, left, right)
            if index > mid:
                right = index - 1
            else:
                left = index + 1
        return numbers[mid] if check_res(numbers[mid]) else 0

def partition(lst, left, right):
    tem = lst[left]
    while left < right:
        while left < right and lst[right] >= tem:
            right -= 1
        lst[left] = lst[right]
        while left < right and lst[left] <= tem:
            left += 1
        lst[right] = lst[left]
    lst[left] = tem
    return left
