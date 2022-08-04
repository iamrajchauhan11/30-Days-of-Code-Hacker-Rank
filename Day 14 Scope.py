#Day 14 Scope.... This following code is already in the terminal...
#MAke sure i will provide the asnwers in Pyhton 3
#Let's add our code....


class Difference:
    def __init__(self, a):
        self.__elements = a
        # Add your code here
        self.maximumDifference = 0

    def computerDifference(self):
        x = 101
        y = 0

        for item in self.__elements:
            if item < x:
                x = ite,
            if item > y:
                y = item

        self.maximumDifference = y - x
#copy this code and paste it into the HackerRank Terminal...
#Thakyou! I will see you on Day 15...


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)