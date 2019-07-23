class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convert_node(self, pNode, pLastNode):
        if not pNode:
            return
        if pNode.left:
            self.convert_node(pNode.left, pLastNode)
        pNode.left = pLastNode.left
        if pLastNode.left:
            pLastNode.left.right = pNode

        pLastNode.left= pNode
        if pNode.right:
            self.convert_node(pNode.right, pLastNode)

    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        pLastNode = TreeNode(0)
        self.convert_node(pRootOfTree, pLastNode)
        pLastNode = pLastNode.left
        while pLastNode.left:
            pLastNode = pLastNode.left
        return pLastNode


if __name__ == "__main__":
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root.left, root.right = node2, node3
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2.left, node2.right = node4, node5

    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node3.left, node3.right = node6, node7
    head = Solution().Convert(root)
    
    while head:
        print(head.val)
        head = head.right
