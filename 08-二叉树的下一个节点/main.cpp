/*
struct TreeLinkNode {
    int val;
    struct TreeLinkNode *left;
    struct TreeLinkNode *right;
    struct TreeLinkNode *next;
    TreeLinkNode(int x) :val(x), left(NULL), right(NULL), next(NULL) {
    }
};
*/
class Solution {
public:

    TreeLinkNode* GetMostLeft(TreeLinkNode* pNode){
        while (pNode->left){
            pNode = pNode->left;
        }
        return pNode;

    }
    TreeLinkNode* GetNext(TreeLinkNode* pNode)
    {
        TreeLinkNode* res = nullptr;
        if (pNode->right){
            res = GetMostLeft(pNode->right);
            return res;
        }
        else if (pNode->next){
            TreeLinkNode* pCur = pNode;
            TreeLinkNode* pPar = pNode->next;
            while (pPar && pPar->right == pCur){
                pCur = pCur->next;
                pPar = pPar->next;
            }
            res = pPar;

        }
        return res;
    }
};
