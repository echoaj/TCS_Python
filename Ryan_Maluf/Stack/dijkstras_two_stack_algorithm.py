from stack import*

equation = "(5+((4+2)*(2+3)))"

operandStack = Stack()
operatorStack = Stack()

for i in equation:
    if i.isdigit():
        operatorStack.push(i)
    if i in ("+", "-", '*', '/'):
        pass