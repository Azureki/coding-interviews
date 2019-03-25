#include <iostream>
class Solution {
public:
  int NumberOf1(int n) {
    n = (n & 0x55555555) + ((n >> 1) & 0x55555555);
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333);
    n = (n & 0x0f0f0f0f) + ((n >> 4) & 0x0f0f0f0f);
    n = (n & 0x00ff00ff) + ((n >> 8) & 0x00ff00ff);
    n = (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff);
    return n;
  }
};

int main() {
  auto soln = Solution();
  int n = -1;
  // nowcoder 上结果是30,但我本地是32
  // 但是如果换成unsigned，nowcoder上是32.
  std::cout << soln.NumberOf1(n) << std::endl;
  return 0;
}
