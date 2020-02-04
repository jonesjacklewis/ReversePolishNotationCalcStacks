#!/usr/bin/env python3
from Stack import Stack  # Imports the Stack class from the Stack file


def reverse_polish_notation():  # defines the function reverse_polish_notation
    reverse_polish_notation_val = Stack()  # Initialises reverse_polish_notation_val as a new Stack object
    operations = ["+", "-", "*", "//", "n", "e"]  # creates a list of possible operands
    effect = "____"  # a variable which will store what is inputted
    print("Enter an operation [+, -, *, //, n, e] or a number")  # informs user of choices
    print("Enter p to calculate and to exit")  # informs user how to get their result
    try:
        while effect != "p":  # runs indented/below code until the 'p' effect is inputted
            effect = input()  # takes the users input and stores in effect
            # Below: if the inputted effect is not an operation and it is also not p run the indented/below code
            if effect not in operations and effect != "p":
                # Below: converts the effect[which will be a number] to a float then pushes to top of the stack
                reverse_polish_notation_val.push(float(effect))
            elif effect != "p":  # else,if, effect is not p
                hold = []  # create a list called hold,this will store the needed numbers
                if effect in operations[:3]:  # if the procedure is in the first 4 positions of the operations list
                    hold.append(reverse_polish_notation_val.pop())  # pop the list and append to hold
                    hold.append(reverse_polish_notation_val.pop())  # pop the list and append to hold
                    equ = "{} {} {}".format(hold[1], effect, hold[0])  # create an equation using string formatting
                    reverse_polish_notation_val.push(eval(equ))  # evaluate the equation and push it to the stack
                else:  # otherwise
                    if effect == "n":  # if the effect is n
                        hold.append(reverse_polish_notation_val.pop())  # pop the list and append to hold
                        reverse_polish_notation_val.push(hold[0]*-1)  # push the 'inverted/negated' form to the stack
                    else:  # otherwise(case e)
                        hold.append(reverse_polish_notation_val.pop())  # pop the list and append to hold
                        hold.append(reverse_polish_notation_val.pop())  # pop the list and append to hold
                        # Below: push the value of hold[1] to the power of hold[0] to the stack
                        reverse_polish_notation_val.push(hold[1]**hold[0])
    except TypeError and ValueError:
        print("Unable to do that")  # informs user that an error has occurred
    if len(reverse_polish_notation()) > 0:
        print(reverse_polish_notation_val.pop())  # remove item from top of stack
    print("Exiting")


reverse_polish_notation()  # run function
end = input()  # take an input to end run

if __name__ == "__main__":
    main()
