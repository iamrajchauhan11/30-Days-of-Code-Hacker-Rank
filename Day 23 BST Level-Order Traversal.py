#HEllo Guys Welcome back again....
#Day 23 BST Level-Order Traversal
#Language Used: Python 3
#So, Below code is laready given in the hacker rank terminal....
#Let's start our coding....



import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        #We have to write our code here...
        if root is None:
            return
        qu = []
        qu.append(root)

        while len(qu) !=0:
            p = qu.pop(0)
            print(p.data, end=' ')
            if p.left is not None:
                qu.append(p.left)
            if p.right is not None:
                qu.append(p.right)
#You havw o write this function in terminal...
#I hope youlike it ... Thankyou for support and wathcing also...
#I will see you next time...
#Thankyou!


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
