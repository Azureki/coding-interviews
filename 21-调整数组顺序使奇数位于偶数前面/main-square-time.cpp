#include <vector>
using namespace std;
class Solution {
public:
  void reOrderArray(vector<int> &array) {
    auto it = array.begin();
    auto last = array.end() - 1;
    for (size_t i = 0; i != array.size(); ++i) {

      if ((*it & 1) == 0) {
        int mask = *it;
        for (auto it2 = it + 1; it2 != array.end(); ++it2) {
          *(it2 - 1) = *it2;
        }
        *last = mask;
      } else {
        ++it;
      }
    }
  }
};
