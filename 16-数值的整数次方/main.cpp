class Solution {
public:
  double Power(double base, int exponent) {
    double mask = base;

    if (exponent > 0) {
      for (; exponent > 1; exponent--) {
        base *= mask;
      }
    } else if (exponent < 0) {
      if (base != 0) {
        for (; exponent < -1; exponent++) {
          base *= mask;
        }
        base = 1 / base;
      }
      // 0^(-n)
      else {
        return 0;
      }
    } else {
      return 1;
    }
    return base;
  }
};

