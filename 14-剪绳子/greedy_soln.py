class Solution:
    def cutRope(self, number):
        if number < 4:
            return number -1
        times_of_3 = number//3
        if number%3==1:
            times_of_3 -= 1
            return 3**times_of_3 * 4
        return 3**times_of_3*2
