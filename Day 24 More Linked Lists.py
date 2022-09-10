#Hello Guys Welcome...
#Day 24 More Linked Lists....
#Language Used: Python 3
#So below code is laready given in the terminal of hacker rank... So let's write our code...



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        #we have o write our code here..
        qu = []
        if head == None:
            return
        p = head
        qu.append(p.data)
        p = p.next
        while p is not None:
            qu.append(p.data)
            p = p.next
        qu = list(dict.fromkeys(qu))
        for item in qu:
            print(item, end=' ')
#You need to write the removeDuplicates function only....
#Thankyou for watching...
#I will see you next time.....

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 