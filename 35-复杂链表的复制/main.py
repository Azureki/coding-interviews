class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    def Clone(self, pHead):
        if not pHead:
            return None
        d = {None: None}
        head = RandomListNode(0)
        cur = RandomListNode(pHead.label)
        head.next = cur
        d[pHead] = cur
        origin_head = pHead
        while pHead.next:
            tem = RandomListNode(pHead.next.label)
            cur.next = tem
            d[pHead.next] = tem
            pHead = pHead.next
            cur = tem
        while origin_head:
            d[origin_head].random = d[origin_head.random]
            origin_head = origin_head.next

        return head.next


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
    print(Solution().Clone(head).label)
