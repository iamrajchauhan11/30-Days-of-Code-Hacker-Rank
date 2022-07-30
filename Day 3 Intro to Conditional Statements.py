#Day 3 conditional Statements... You will see this type of code in Python Terminal..
#Sooo, Let's Start Coding

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    #Put some Conditions..
    if N%2 != 0:
        print('Weird')
    elif N%2 == 0 and N in range(2, 6):
        print('Not Weird')
    elif N%2 == 0 and N in range(6, 21):
        print('Weird')
    elif N%2 == 0 and N>20:
        print('Not Weird')

#Put these Conditions and Just Submit.....
#Thankyou!! i will see you on next Day....