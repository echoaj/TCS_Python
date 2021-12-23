from stack import*


# check if equation is correctly parenthesized
s2 = Stack()
equation = "((8+3)+(4-3))"
underflow = False

for i in equation:
    if i == "(":
        s2.push(i)
    elif i == ")":
        underflow = s2.is_empty()
        s2.pop()

if s2.length() == 0 and not underflow:
    print("\n\nCorrectly Parenthesized")
else:
    print("\n\nNot Correctly Parenthsized")
