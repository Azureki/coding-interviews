class Solution {
public:
    int rectCover(int n) {
        int result[2] = {0, 1};
        if (n < 2){
            return result[n];
        }
        int fib_minus_two = 1;
        int fib_minus_one = 1;
        int fib_n = 0;
        for (unsigned i = 2; i <= n; ++i){
            fib_n = fib_minus_one + fib_minus_two;
            fib_minus_two = fib_minus_one;
            fib_minus_one = fib_n;
        }
        return  fib_n;
    }
};

