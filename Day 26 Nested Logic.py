#Hello Guys Welcome back again
#Day 26 Nested Logic...
#Language Used: Pyhton 3
#Let's start coding...

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
x = list(map(int, n.split()))
m = input()
y = list(map(int, m.split()))
z = 0

if y[2] < x[2]:
    z = 10000
elif y[2] == x[2]:
    if y[1] < x[1]:
        z = 500*(x[1]-y[1])
    elif y[0] < x[0]:
        z = 15*(x[0]-y[0])

print(z)

#You have to write this code in the hacker rank terminal...
#All the program files are in the description just one click and download it..
#Thankyou for watching..
#KEEP CODING AND KEEP LEARNING..
#I will see you next time./