#include <iostream>
using namespace std;
struct ListNode {
  int val;
  struct ListNode *next;
  ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
  ListNode *FindKthToTail(ListNode *pListHead, unsigned int k) {
    // 倒数k，正数是N - (k -1)
    // west need to move N - (k -1) -1 == N-k steps.
    // hk need to start again at N - (N -k) == k.
    // hk firstly move k -1 steps.

    // 如果为空
    if (!pListHead || k == 0) {
      return nullptr;
    }

    ListNode *hk, *west;
    hk = west = pListHead;
    // 不能从0开始，k可能为0,k-1不是-1。
    for (unsigned int i = 1; i < k; ++i) {
      // 如果为空
      if (!hk->next) {
        return nullptr;
      }
      hk = hk->next;
    }
    while (hk->next) {
      hk = hk->next;
      west = west->next;
    }
    return west;
  }
};

// 事实上，如果直接传个-1,那就没办法了。
void test(unsigned int n) { cout << n << endl; }

int main() {
  int n = -1;
  test(n);
  return 0;
}
