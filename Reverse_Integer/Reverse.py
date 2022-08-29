# This is a sample Python script.
"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
Example 2:
Input: x = -123
Output: -321
"""


class Reverse:

    def __int__(self, number):  # self
        self.number = number

    def reverse(self, retrun=list):  # to reverse the given number
        n = 0
        list = []
        for i in range(0, 10):
            if self.number < 10 ** i:
                n = i
                break
        for i in range(1, n):
            list[0] = self.number % 10
            list[i] = (self.number % (10 ** (i + 1)) - self.number % (10 ** i)) / (10 ** i)

        retrun[list]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num = int(input())
    ls = Reverse(num)
    print(ls.revers())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
