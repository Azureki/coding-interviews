struct ListNode {
  int val;
  struct ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};
class Solution {
public:
  ListNode *Merge(ListNode *pHead1, ListNode *pHead2) {
    ListNode mask = ListNode(0);
    ListNode *res = &mask;
    while (pHead1 && pHead2) {
      // res->next = pHead1->val>pHead2->val?pHead1:pHead2;
      if (pHead1->val < pHead2->val) {
        res->next = pHead1;
        res = res->next;
        pHead1 = pHead1->next;
      } else {
        res->next = pHead2;
        res = res->next;
        pHead2 = pHead2->next;
      }
    }
    while (pHead1) {
      res->next = pHead1;
      res = res->next;
      pHead1 = pHead1->next;
    }
    while (pHead2) {
      res->next = pHead2;
      res = res->next;
      pHead2 = pHead2->next;
    }
    return mask.next;
  }
};
