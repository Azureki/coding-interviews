#include <bits/stdc++.h>
using namespace std;
struct TreeNode {
  int val;
  struct TreeNode *left;
  struct TreeNode *right;
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
class Solution {
public:
  void Mirror(TreeNode *pRoot) {
    stack<TreeNode *> stk;
    while (true) {
      while (pRoot) {
        TreeNode *tem = pRoot->left;
        pRoot->left = pRoot->right;
        pRoot->right = tem;
        stk.push(pRoot);
        pRoot = pRoot->left;
      }
      if (stk.empty()){
        return;
      }
      pRoot = stk.top()->right;
      stk.pop();
    }
  }
};
