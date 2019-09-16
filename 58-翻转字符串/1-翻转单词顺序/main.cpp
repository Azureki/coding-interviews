#include <string>
using namespace std;
class Solution {
public:
    void reverseString(string::iterator left, string::iterator right) {
        while (left < right) {
            swap(*(left++), *(--right));
        }
    }
    string ReverseSentence(string str) {
        auto begin = str.begin();
        auto end = str.end();
        reverseString(begin, end);
        begin = end = str.begin();
        while (begin != str.end()) {
          if (*begin == ' ') {
            ++begin;
            ++end;
          } else if (*end == ' ' || end == str.end()) {
            reverseString(begin, end);
            begin = end;
          } else {
            ++end;
          }
        }
        return str;
    }
};
