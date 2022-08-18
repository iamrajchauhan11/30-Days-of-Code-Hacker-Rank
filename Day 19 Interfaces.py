#Hello Guys..
#Day 19 Interfaces...
#LAnguage used Python 3
#The below code is already written in the terminal...
#Let's start coding...



class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        #We need to write our code here. Before writing we need to erase pass...
        temp = []
        for i in range(1, n+1):
            if n%i == 0:
                temp.append(i)
        return sum(temp)
#We need to only write above code...


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)


#Thankyou for watching....
#I will see you on next day....
#KEEP CODING KEEP LEARNING...

#Programming files are in Description you can download them directly....