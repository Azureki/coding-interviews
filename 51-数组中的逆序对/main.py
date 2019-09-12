def merge_sort(array):
    aux = array[:]
    return __merge_sort__(aux, array, 0, len(array)) % 1000000007


def __merge_sort__(src, dst, left, right):
    if right <= left + 1:
        return 0
    mid = (left + right) // 2
    res = 0
    res += __merge_sort__(dst, src, left, mid)
    res += __merge_sort__(dst, src, mid, right)
    res += merge(src, dst, left, right)
    return res


def merge(src, dst, lo, hi):
    res = 0
    mid = (lo + hi) // 2
    # left half: [lo, mid), right half: [mid, right)
    left, right = mid - 1, hi - 1
    for i in range(hi - 1, lo - 1, -1):
        if right < mid or left >= lo and src[left] > src[right]:
            res += right - mid + 1
            dst[i] = src[left]
            left -= 1

        else:
            dst[i] = src[right]
            right -= 1
    return res


class Solution:
    def InversePairs(self, data):
        return merge_sort(data)


lst = [23, 234, 456, 2, 376, 879]
lst = [7, 5, 6, 4]
lst = [1, 2, 3, 4, 5, 6, 7, 0]
res = merge_sort(lst)
# print(lst)
print(res)
