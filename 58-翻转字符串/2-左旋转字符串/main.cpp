#include <string>
using namespace std;
class Solution {
public:
    void reverseString(string &s, int left, int right) {
        while (left < right) {
            swap(s[left++], s[--right]);
        }
    }
    string LeftRotateString(string str, int n) {
        if (n < 0 || n > str.size()){
            return str;
        }
        string res = str;
        reverseString(res, 0, n);
        reverseString(res, n, str.size());
        reverseString(res, 0, str.size());
        return res;
    }
};

