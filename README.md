# ReversePolishNotationCalcStacks
A Reverse Polish Notation Calculator that uses stacks.

The Stack.py file has a class which lets us simulate a stack using a list. It has 5 different functions. A "__init__" function which initialises out 'stack'. There is also a "push" function which pushes and item to the stack. A "pop" function which removes the item at the top of the stack. An "isEmpty" function which verifies whether the stack is empty. There is also a "top" function which returns the item at the top of the stack.

class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,elem):
        self.stack.append(elem)

    def pop(self):
        if len(self.stack)==0:
            return None
        else:
            return self.stack.pop()

    def isEmpty(self):
        if len(self.stack)==0:
            return True
        return False

    def top(self):
        return self.stack[-1]
