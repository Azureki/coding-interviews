# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def get_linklist_len(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def FindFirstCommonNode(self, pHead1, pHead2):
        length1 = self.get_linklist_len(pHead1)
        length2 = self.get_linklist_len(pHead2)
        # assume linklist1.len < linklist2.len
        dif = length2 - length1
        if length1 > length2:
            pHead1, pHead2 = pHead2, pHead1
            dif = length1 - length2
        for i in range(dif):
            pHead2 = pHead2.next
        while pHead1 != pHead2:
            pHead1 = pHead1.next
            pHead2 = pHead2.next

        return pHead1

