from Stack import Stack
def RPN():
    rpn_val=Stack()
    operations=["+","-","*","//","n","e"]
    effect="____"
    print("Enter p to exit")
    while effect!="p":
        effect=input()
        if effect=="p":
            operations.append(".")
        if effect not in operations and effect!="p":
            rpn_val.push(float(effect))
        elif effect!="p":
            hold=[]
            if effect in operations[:3]:
                hold.append(rpn_val.pop())
                hold.append(rpn_val.pop())
                equ="{} {} {}".format(hold[1],effect,hold[0])
                rpn_val.push(eval(equ))
            else:
                if effect=="n":
                    hold.append(rpn_val.pop())
                    rpn_val.push(hold[0]*-1)
                else:
                    hold.append(rpn_val.pop())
                    hold.append(rpn_val.pop())
                    rpn_val.push(hold[1]**hold[0])
                    
    print(rpn_val.pop())
    return None

RPN()
input()
