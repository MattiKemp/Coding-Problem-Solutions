#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'movingTiles' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER s1
#  3. INTEGER s2
#  4. INTEGER_ARRAY queries
#
# Runtime: O(n) where n is the number of queries.
# Space: O(n), where n is the number of queries, if we don't count the 
# space required for the answer: O(1)
def movingTiles(l, s1, s2, queries):
    diffVel = math.sqrt((abs(s2 - s1)**2)/2)
    queryAnswers = [0 for x in queries]
    for i in range(len(queries)):
        queryAnswers[i] = (l - math.sqrt(queries[i]))/diffVel
    return queryAnswers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    l = int(first_multiple_input[0])

    s1 = int(first_multiple_input[1])

    s2 = int(first_multiple_input[2])

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

