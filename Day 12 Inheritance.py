#Day 12 Inheritance...... This given code is already in the terminal...
#we have to write the function....
#Let's star coding....

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def __init__(self, firstName, lastName, idNum, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNum
        self.scores = scores
        
        def printPerson(self):
            print("Name: " + lastName + ", " + firstName)
            print("ID:", idNum)

        def calculate(self):
            x = len(scores)
            n = 0
            for i in range(x):
                n+=scores[i]

            y = int(n)//int(x)

            if 90<= y <= 100:
                return '0'

            elif 80<= y < 90:
                return 'E'
            
            elif 70<= y < 80:
                return 'A'
            
            elif 55<= y <70:
                return 'P'

            elif 40<= y < 55:
                return 'D'

            else:
                return 'T'

#This code is too long so i suggest you to download the file from the description and then copy and paste this code into the  Hacker Rank Terminal
# thankyou!!! I will see you in next problem....             






line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())