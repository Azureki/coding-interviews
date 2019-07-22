"""
1. 复制
2. sibling/random
3. 分离两个链表
"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def Clone(self, pHead):
        if not pHead:
            return None
        cur = pHead
        while cur:
            tem = RandomListNode(cur.label)
            tem.next = cur.next
            cur.next = tem
            cur = tem.next

        cur = pHead
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        cur = pHead
        res = pHead.next
        head = res
        cur.next = head.next
        cur = cur.next
        while cur:
            head.next = cur.next
            head = head.next
            print(cur.label)
            cur.next = head.next
            cur = cur.next

        return res


if __name__ == '__main__':
    head = RandomListNode(1)
    node2 = RandomListNode(2)
    head.next = node2
    node3 = RandomListNode(3)
    node2.next = node3
    node4 = RandomListNode(4)
    node3.next = node4
    node5 = RandomListNode(5)
    node4.next = node5
    head = Solution().Clone(head)
    print("########")
    while head:
        print(head.label)
        head=head.next
