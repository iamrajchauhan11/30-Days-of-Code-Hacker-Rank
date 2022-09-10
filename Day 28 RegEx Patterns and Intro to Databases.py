#Hello Guys Welcome back again..
#Day 28 RegEx Patterna and Intro to Databases....
#Let's start coding and please see carefully..



#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    nw = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        if '@gmail.com' in emailID:
            nw.append(firstName)

    nw = sorted(nw)
    for item in nw:
        print(item)
#Done...you have to write this code in the hacker rank terminal...
#Thankyou for the support ...KEEP CODING AND KEEP LEARNING...
#I will see you on last day of our Day 30 Series....

