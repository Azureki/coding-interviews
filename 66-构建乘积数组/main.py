class Solution:
    def multiply(self, A):
        length = len(A)
        lst_c = [1] * length
        lst_d = [1] * length
        for i in range(1, length):
            lst_c[i] = lst_c[i - 1] * A[i - 1]
        for i in range(length - 1, 0, - 1):
            lst_d[i - 1] = lst_d[i] * A[i]
        return [lst_c[i] * lst_d[i] for i in range(length)]

# Actually, only one array(lst_c or lst_d) is needed.

lst = [1,2,3,4,5]
res = Solution().multiply(lst)
print(res)
