#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def primeCount(n):
    # the max input size is 10^18 so we need to find the primoral value < max n.
    # Since the primorial function grows quicker than the factorial function 
    # the max value uses a small number of primes. Because of this, it is more efficent
    # to just hard code all the primes up to the max value instead of sieveing them.
    # One way to circumvent hardcoding in the primes would be to write a function
    # that takes all the different inputs, sieves the required primes from the max, and then
    # processes all of them. This would have a nearly equivalent runtime to the below solution.
    # runtime: O(1) for each input, O(m), for all inputs.
    # memory: O(1) for both.
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
    primorial = 1
    spot = 0
    while(primorial <= n):
        primorial *= primes[spot]
        spot += 1
    return spot - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()

