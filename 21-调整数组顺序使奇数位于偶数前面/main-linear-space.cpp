#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
  static bool isEven(int num) {
    // return num % 2 == 0;
    return (num & 1) == 0;
  }
  void reOrder(vector<int> &array, bool (*judge)(int)) {
    vector<int> vec(array.size());

    auto odd = array.begin();
    auto even = vec.begin();
    for (auto it = array.begin(); it != array.end(); it++) {
      if (judge(*it)) {
        *even = *it;
        even++;
      } else {
        *odd = *it;
        odd++;
      }
    }

    for (auto it = array.end(); even != vec.begin();) {
      *--it = *--even;
    }
  }

  void reOrderArray(vector<int> &array) { reOrder(array, isEven); }
};
