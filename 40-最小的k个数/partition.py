class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        index = 0
        left, right = 0, len(tinput) - 1
        while left < right:
            index = partition(tinput, left, right)
            if index < k:
                left = index + 1
            else:
                right = index - 1
        return sorted(tinput[:k]) if len(tinput) >= k else []


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


if __name__ == '__main__':
    lst = [4, 5, 1, 6, 2, 7, 3, 8]
    res = Solution().GetLeastNumbers_Solution(lst, 4)
    print(res)
