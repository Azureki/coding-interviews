from collections import defaultdict


class Solution:
    def FirstNotRepeatingChar(self, s):
        d = defaultdict(int)
        # from collections import Counter
        # d = Counter(s)
        for c in s:
            d[c] += 1
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1
