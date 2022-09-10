#Hello Guys Welcome back to my channel...
#Day 25 Running Time and Complexity...
#Language used: Python 3
#LEt's start coding..

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt

T = int(input())

def isPrime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i is 0:
            return False
    return True

for _ in range(T):
    n = int(input())

    if n >= 2 and isPrime(n):
        print("Prime")

    else:
        print("Not Prime")

#This is the solution of day 25...
#Thankyou for the support Keep watching and keep learning...
#I will see you next time....