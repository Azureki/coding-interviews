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
    auto even = array.begin();
    auto odd = array.end();
    while (even < odd) {
      while (even < odd && !judge(*even)) {
        ++even;
      }
      while (even < odd && judge(*--odd)) {
      }
      // iter_swap(even, odd);
      swap(*even, *odd);
    }
  }

  void reOrderArray(vector<int> &array) { reOrder(array, isEven); }
};
