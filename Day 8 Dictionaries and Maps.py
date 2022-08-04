#Day 8 Dictionaries and Maps.... 
#LEt's start coding

# Enter your code here. Read input from STDIN. Print output to STDOUT

x = int(input())

dictt = {}

for i in range(x):
    text = input().split()
    dictt[text[0]] = text[1]

while True:
    try:
        inpt = input()
        if inpt in dictt:
            print(inpt+"="+dictt[inpt])
        else:
            print("Not Found")

    except EOFError:
        break

#Copy and Paste this code in Hacker Rank TErminal...
#Thankyou! for Watching.