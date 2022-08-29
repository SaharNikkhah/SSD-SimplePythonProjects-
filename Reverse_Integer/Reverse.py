
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
#FOR SNA!! WELL I THINK IT'S WORKING EXCEPT FOR THE PART THAT IT IS NOT SIGN SENSETIVE AND 32 BIT BIGGER?


class Reverse:
    def __init__(self, number):  # self
        self.number = number

    def reverse(self):  # to reverse the given number
        n = 0
       #I am stupid!!

       #for i in range(0, 10):
        #    if self.number < (10 ** i):
         #       n = i
          #      break

        #list.append(self.number % 10)
        #for i in range(1, n):

         #   list.append((self.number % (10 ** (i + 1)) - self.number % (10 ** i)) / (10 ** i))
        #reversed=0
        #for i, value in enumerate(list):#thanks to you :D
         #   reversed+=10**i*list[n-i-1]
        #This is a smarter way!
        List1 = list(str(self.number))

        print("".join(List1[::-1]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num = int(input())
    ls = Reverse(num)
    ls.reverse()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
