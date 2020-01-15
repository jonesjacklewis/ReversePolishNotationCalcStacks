#!/usr/bin/env python3
from Stack import Stack#Imports the Stack class from the Stack file
def RPN():#defines the function RPN
    rpn_val=Stack()#Initialises rpn_val as a new Stack object
    operations=["+","-","*","//","n","e"]#creates a list of possible opperands 
    effect="____"#a variable which will store what is inputted
    print("Enter p to exit")#informs user how to get their result
    while effect!="p":#runs indented/below code until the 'p' effect is inputted
        effect=input()#takes the users input and stores in efect
        if effect not in operations and effect!="p":#if the inputted effect is not an operation and it is also not p run the indented/below code
            rpn_val.push(float(effect))#converts the effect[which will be a number] to a float then pushes to top of the stack
        elif effect!="p":#else,if, effect is not p
            hold=[]#create a list called hold,this will store the needed numbers
            if effect in operations[:3]:#if the procedure is in the first 4 positions of the operations list
                hold.append(rpn_val.pop())#pop the list and append to hold
                hold.append(rpn_val.pop())#pop the list and append to hold
                equ="{} {} {}".format(hold[1],effect,hold[0])#create an equation using string formatinng
                rpn_val.push(eval(equ))#evaluate the equation and push it to the stack
            else:#otherwise
                if effect=="n":#if the effect is n
                    hold.append(rpn_val.pop())#pop the list and append to hold
                    rpn_val.push(hold[0]*-1)#push the 'inverted/negated' form to the stack
                else:#otherwise(case e)
                    hold.append(rpn_val.pop())#pop the list and append to hold
                    hold.append(rpn_val.pop())#pop the list and append to hold
                    rpn_val.push(hold[1]**hold[0])#push the value of hold[1] to the power of hold[0] to the stack
                    
    print(rpn_val.pop())#remove item from top of stack
    return None#return None

RPN()#run function
input()#take an input
