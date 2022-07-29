#Day 2 Operators, In Pyhton Terminal you will find this Code...
#Soo Let's Start Coding

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    total_cost = meal_cost + meal_cost * tip_percent/100 + meal_cost *tax_percent/100
    print(round(total_cost)) #<= round() is used for round the decimal figure in nearby number.
#Type this code only ....


if __name__ == '__main__':
    
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)

#Thankyou! See you on next Day with New Problem Day 3....