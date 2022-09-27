import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left = 0
    right = 0
    for i in range(len(arr)):
        left += arr[i][i]
        right += arr[i][len(arr) - (i + 1)]
    return abs(left - right)


if __name__ == '__main__':
    arr = [[11,2,4],[4,5,6],[10,9,-12]]
    print(diagonalDifference(arr))
