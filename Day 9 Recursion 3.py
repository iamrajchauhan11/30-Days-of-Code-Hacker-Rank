#Day 9 REcursion..... This given code is already in Terminal of Hacker Rank
#We just write a function..
#Let's start coding


#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the 'factorial' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.

# Write your code here
def factorial(n):
    if n == 1:
        return 1
    else:
        n = n * factorial(n-1)
    return n
#type this code in terminal....
#thankyou! for watching...

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
