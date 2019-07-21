class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def dfs(self, root, expectNumber):
        expectNumber -= root.val
        self.path.append(root.val)
        if not root.left and not root.right and expectNumber == 0:
            self.res.append(self.path[:])

        if root.left:
            self.dfs(root.left, expectNumber)
        if root.right:
            self.dfs(root.right, expectNumber)

        self.path.pop()

    def FindPath(self, root, expectNumber):
        if not root:
            return []
        self.dfs(root, expectNumber)
        return self.res


root = TreeNode(10)
node1 = TreeNode(5)
node2 = TreeNode(12)
root.left, root.right = node1, node2
node1.left, node1.right = TreeNode(4), TreeNode(7)

s=Solution()
res = s.FindPath(root, 22)
print(res)
res = s.FindPath(root, 15)
print(res)
