class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        for i in range(len(numbers)):
            while numbers[i] != i:
                tem = numbers[i]
                if numbers[tem] == tem:
                    duplication[0] = tem
                    return True
                numbers[i], numbers[tem] = numbers[tem], numbers[i]
        return False
