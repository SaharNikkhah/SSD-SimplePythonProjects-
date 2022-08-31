
"""Given an array of integers, where all elements but one occur twice, find the unique element."""
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a, n):
    # a.sort()

    res = a[0]

    # Do XOR of all elements and return
    for i in range(1, n):
        res = res ^ a[i]

    return res

    # Write your code here


if __name__ == '__main__':


    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a, n)

    print(str(result) + '\n')

