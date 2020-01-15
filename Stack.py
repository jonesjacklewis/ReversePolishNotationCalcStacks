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
