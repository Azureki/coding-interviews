#include <queue>
#include <vector>
using namespace std;
/*
struct TreeNode {
        int val;
        struct TreeNode *left;
        struct TreeNode *right;
        TreeNode(int x) :
                        val(x), left(NULL), right(NULL) {
        }
};*/
class Solution {
public:
  vector<int> PrintFromTopToBottom(TreeNode *root) {
    if (!root) {
      return vector<int>{};
    }
    vector<int> res;
    queue<TreeNode *> q;
    q.push(root);
    while (q.size()) {
      TreeNode *mask = q.front();
      res.push_back(mask->val);
      q.pop();
      if (mask->left) {
        q.push(mask->left);
      }
      if (mask->right) {
        q.push(mask->right);
      }
    }
    return res;
  }
};
