class Solution:
    def movingCount(self, threshold, rows, cols):
        digit_sum = lambda x: sum(map(int, str(x)))
        two_sum = lambda x, y: digit_sum(x) + digit_sum(y)

        def dfs(row, col):
            if not (0 <= row < rows and 0 <= col < cols and
                    not visited[row][col] and two_sum(row, col) <= threshold):
                return 0
            visited[row][col] = True
            dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            return 1 + sum(dfs(row + d[0], col + d[1]) for d in dirs)

        visited = [[False] * cols for _ in range(rows)]
        return dfs(0, 0)
