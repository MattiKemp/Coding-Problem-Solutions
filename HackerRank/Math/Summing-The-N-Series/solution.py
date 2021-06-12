#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'summingSeries' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

# the series simplifies to the sum of the nth odd integer, which is just n^2.
# Since python does not have a small max integer size, (I believe it is bounded by your machine/interpreter's
# word size limit, which is huge) we don't really need to worry about the size of n^2 as it won't overflow
# given reasonable inputs and the algorithms for multiplication and moduli are implemented really fast.
# See the c++ solution for a bounded int size solution.
def summingSeries(n):
    return n*n % (10**9 + 7)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = summingSeries(n)

        fptr.write(str(result) + '\n')

    fptr.close()

