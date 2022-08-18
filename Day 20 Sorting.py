#Hello Guys...
#Day 20 Sorting.....
#Language Used Pyhton 3
#Below code is already written in the terminal....
#Let's start coding.....



import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    nofswap = 0
for i in range(0, n-1):
    for i in range(0,n-1):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
            nofswap += 1
print("Array is sorted in", nofswap, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[-1])

#You need to write above code in the terminal...
#Thankyou for Watching...
#I will see you on next day...
#KEEP CODING KEEP LEARNING
