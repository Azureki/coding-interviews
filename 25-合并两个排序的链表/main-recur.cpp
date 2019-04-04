/* 因为是递归，O(N)空间复杂度 */

struct ListNode {
  int val;
  struct ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};
class Solution {
public:
  ListNode *Merge(ListNode *pHead1, ListNode *pHead2) {
    if (!pHead1) {
      return pHead2;
    } else if (!pHead2) {
      return pHead1;
    }
    if (pHead1->val < pHead2->val) {
      pHead1->next = Merge(pHead1->next, pHead2);
      return pHead1;
    } else {
      pHead2->next = Merge(pHead1, pHead2->next);
      return pHead2;
    }
  }
};
