class Solution:
    def number_of_1(self, str_n):

        if not str_n:
            return 0
        if str_n[0]=='0':
            return self.number_of_1(str_n[1:])
        if len(str_n) == 1:
            return 0 if str_n[0] == '0' else 1
        first_digit = int(str_n[0])
        num_first_digit = 10**(len(str_n) - 1) if first_digit > 1 else int(str_n[1:]) + 1
        num_other_digits = first_digit * (len(str_n) - 1) * 10**(len(str_n) - 2)
        print(str_n, num_first_digit, num_other_digits)
        return num_first_digit + num_other_digits + self.number_of_1(str_n[1:])

    def NumberOf1Between1AndN_Solution(self, n):
        return self.number_of_1(str(n))

Solution().NumberOf1Between1AndN_Solution(10000)
