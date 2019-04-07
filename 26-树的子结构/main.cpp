struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
class Solution {
public:
  bool IsSub(TreeNode *pRoot1, TreeNode *pRoot2) {
    if (!pRoot2){
      return true;
    }
    if (!pRoot1){
      return false;
    }
    if (pRoot1->val == pRoot2->val) {
      return IsSub(pRoot1->left, pRoot2->left) && IsSub(pRoot1->right,pRoot2->right);
    }
    return false;
  }
  bool HasSubtree(TreeNode *pRoot1, TreeNode *pRoot2) {
    if (!pRoot2||!pRoot1){
      return false;
    }
    // if ((pRoot1->val == pRoot2->val) && IsSub(pRoot1, pRoot2)) {
    if (IsSub(pRoot1, pRoot2)) {
      return true;
    }
    return HasSubtree(pRoot1->left, pRoot2) ||
           HasSubtree(pRoot1->right, pRoot2);
  }
};
