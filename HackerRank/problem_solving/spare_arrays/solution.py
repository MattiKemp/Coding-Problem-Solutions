#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    # basic use of dictionary, don't think there is a much better solution.
    # runtime: O(n+m), where n is the length of strings and m is the length of queries.
    # memory: O(n+m), where n is the length of strings and m is the length of queries.
    # if you don't count the output array then the memory is: O(n).
    inputDict = {x:0 for x in strings}
    for i in strings:
        inputDict[i] += 1
    output = [0 for x in range(len(queries))]
    for i in range(len(queries)):
        if inputDict.get(queries[i]) != None:
            output[i] += inputDict[queries[i]]
    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

