class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        def check_res(tar):
            return sum(x == tar for x in numbers) > len(numbers) // 2

        if not numbers:
            return 0
        count, cur = 0, None
        for x in numbers:
            if cur == x:
                count += 1
            elif count == 0:
                cur = x
                count += 1
            else:
                count -= 1
        return cur if check_res(cur) else 0


if __name__ == '__main__':
    lst = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print(Solution().MoreThanHalfNum_Solution(lst))
