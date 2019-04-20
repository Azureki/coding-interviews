#include <vector>
using namespace std;

class Solution {
public:
  vector<int> printMatrix(vector<vector<int>> matrix) {
    vector<int> res(0);
    if (!matrix.size() || !matrix[0].size()) {
      return res;
    }
    int size = matrix.size();
    int length = matrix[0].size();
    int nums = size * length;
    res.resize(nums);

    int d = 0;
    int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    int left = -1, right = length, top = -1, bottom = size;
    for (int i = 0, x = 0, y = 0; i < nums; ++i) {
      res[i] = matrix[x][y];
      x += dirs[d][0];
      y += dirs[d][1];

      if (y == left) {
        --bottom;
      } else if (y == right) {
        ++top;
      } else if (x == top) {
        ++left;
      } else if (x == bottom) {
        --right;
      } else {
        continue;
      }

      x -= dirs[d][0];
      y -= dirs[d][1];
      d = (d + 1) % 4;
      x += dirs[d][0];
      y += dirs[d][1];
    }
    return res;
  }
};
