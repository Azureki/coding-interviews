#include <stack>
using namespace std;
class Solution {
public:
  void push(int value) {
    this->m_data.push(value);
    if (this->m_min.empty() || value < this->m_min.top()) {
      this->m_min.push(value);
    } else {
      this->m_min.push(this->m_min.top());
    }
  }
  void pop() {
    this->m_data.pop();
    this->m_min.pop();
  }
  int top() { return this->m_data.top(); }
  int min() { return this->m_min.top(); }

private:
  stack<int> m_data;
  stack<int> m_min;
};
