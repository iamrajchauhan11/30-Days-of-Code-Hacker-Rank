#Hello Guys.... Welcome back....
# Day 22 Binary Search Trees...
# Language Used: Python 3
#So, Below code is already given in the hacker rank terminal..
#Lets start coding...



from colorsys import hls_to_rgb
from ctypes import HRESULT
from urllib.parse import non_hierarchical


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

    def getHeight(self,root):
        #Write your code here
        #We have to write our function here...
        if root is None:
            return -1
        
        hL = self.getHeight(root.left)
        hR = self.getHeight(root.right)

        if hL > hR:
            return 1+hL
        else:
            return 1+hR

#Thats it you have to write this fucntion only...
#Thankyou for watching...
# I will see you next time...
# Thankyou!        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       