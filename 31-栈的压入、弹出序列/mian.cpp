#include <iostream>
#include <stack>
#include <vector>
using namespace std;
class Solution {
public:
  bool IsPopOrder(vector<int> pushV, vector<int> popV) {
    stack<int> stk;
    auto push_it = pushV.begin();
    for (auto it = popV.begin(); it != popV.end(); ++it) {
      // stk is empty
      if (stk.empty()) {
        while (push_it != pushV.end() && *push_it != *it) {
          stk.push(*push_it);
          // cout << "push " << *push_it << endl;
          ++push_it;
        }
        ++push_it;

      }
      // stk is not empty
      else {
        // top is not equal
        if (stk.top() != *it) {
          while (push_it != pushV.end() && *push_it != *it) {
            stk.push(*push_it);
            // cout << "push " << *push_it << endl;
            ++push_it;
          }
          ++push_it;
        }
        // top is equal
        else {
          // cout << "pop " << stk.top() << endl;
          stk.pop();
        }
      }
    }
    return stk.empty();
  }
};

int main() {
  // vector<int> pushV{1, 2, 3, 4, 5};
  // vector<int> popV{4, 3, 5, 1, 2};
  vector<int> pushV{2};
  vector<int> popV{4};

  bool res = Solution().IsPopOrder(pushV, popV);
  cout << res << endl;

  return 0;
}
