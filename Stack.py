#!/usr/bin/env python3
class Stack: #Creates a Class called Stack
    def __init__(self):#ran when an object is initialised
        self.stack=[]#creates a list which will be used to model a stack

    def push(self,elem):
        self.stack.append(elem)#pushes elem to the top of the stack

    def pop(self):
        if len(self.stack)==0:
            return None
        else:
            return self.stack.pop()#returns and removes item at top of the stack

