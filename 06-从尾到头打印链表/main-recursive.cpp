/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/
class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        vector<int> res;
        soln(res,head);
        return res;
    }
    void soln(vector<int> &res,ListNode* head){
        if (!head){
            return;
        }
        soln(res,head->next);
        res.push_back(head->val);
    }
};
