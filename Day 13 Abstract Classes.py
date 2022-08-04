#Day 13 Abstract Classes...... this following code is given in Hacker Rank Terminal...
#Let's make the MyBook CLass and start coding...
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", title)
        print("Auhtor:", author)
        print("Price:", price)

#Copy this code and paste it into the Hacker Rank Terminal....
#Thankyou! I will see you tommorrow....





title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()