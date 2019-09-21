class Solution:
    def hasPath(self, matrix, rows, cols, path):
        def dfs(row, col, path_len):
            if path_len == len(path):
                return True
            has_path = False
            if (0 <= row < rows and 0 <= col < cols
                    and matrix[row][col] == path[path_len]
                    and not visited[row][col]):
                path_len += 1
                visited[row][col] = True
                has_path = (dfs(row, col + 1, path_len)
                            or dfs(row, col - 1, path_len)
                            or dfs(row + 1, col, path_len)
                            or dfs(row - 1, col, path_len))
                if not has_path:
                    visited[row][col] = False
            return has_path

        matrix = [matrix[i*cols:(i+1)*cols] for i in range(rows)]
        path_len = 0
        visited = [[False] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, path_len):
                    return True

        return False


matrix = [
    ['a', 'b', 'c', 'e'],
    ['s', 'f', 'c', 's'],
    ['a', 'd', 'e', 'e']
]
path = 'bcced'
matrix, rows, cols, path = "ABCESFCSADEE", 3, 4, "ABCCED"
matrix = [matrix[i * cols:(i + 1) * cols] for i in range(rows)]
res = Solution().hasPath(matrix, rows, cols, path)
print(res)
