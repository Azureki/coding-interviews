/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* ReverseList(ListNode* pHead) {
      if (!pHead || !pHead->next){
        return pHead;
      }
      ListNode *res = ReverseList(pHead->next);
      pHead->next->next = pHead;
      pHead->next = nullptr;
      return res;
    }
};
