#Hello Guys!
#Day 17 More Exceptions...... So let's start coding
#Language Pyhton 3



#Write your code here
class Claculator:
    def power(self,n,p):
        if n < 0 or p < 0:
            raise Exception("n and p should be non-negative")
        else:
            return pow(n,p)

#You need to write above code only....


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e) 

#Thankyou Guys I will see you on next day...
#KEEP CODING KEEP LEARNING.....