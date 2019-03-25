#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    void push(int node) {
        stack1.push(node);
    }

    int pop() {
        int res;
        if (stack2.empty()){
            while (!stack1.empty()){
                int tem = stack1.top();
                stack1.pop();
                stack2.push(tem);
            }
            res = stack2.top();
            stack2.pop();
        }
        else{
            res = stack2.top();
            stack2.pop();
        }
        return res;
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};

