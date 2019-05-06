class Solution:
    def find_first_right(self, lst, num):
        for i, x in enumerate(lst):
            if x > num:
                return i
        return i

    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        return self.VerifySquenceOfBST2(sequence)

    def VerifySquenceOfBST2(self, sequence):
        if not sequence:
            return True

        root = sequence[-1]
        right = self.find_first_right(sequence, root)
        if min(sequence[right:]) < root:
            return False

        return self.VerifySquenceOfBST2(
            sequence[:right]) and self.VerifySquenceOfBST2(sequence[right:-1])
