#!/bin/python3
""" Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not."""
import math
import os
import random
import re
import sys


#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    for i in range(len(grid)):
        res = ''.join(sorted(grid[i]))
        grid[i] = res
        print(grid[i])
    # print(grid)
    ans = 'YES'
    #loop over grids columns
    for i in range(len(grid)):
        for x in range(len(grid[0])):
            s = ''.join(i[x] for i in grid)
            y = ''.join(sorted(s))
            if s != y:
                ans = 'NO'

    return (ans)  # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
