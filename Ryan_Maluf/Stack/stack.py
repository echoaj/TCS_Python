
class Stack:
    def __init__(self):
        self.__array = []

    def pop(self):
        if not self.is_empty():
            self.__array.pop()
        else:
            print("stack is empty")

    def push(self, data):
        self.__array.append(data)

    def peek(self):
        if not self.is_empty():
            return self.__array[-1]
        else:
            return "stack is empty"

    def length(self):
        return len(self.__array)

    def is_empty(self):
        return not bool(self.length())

    def display(self):
        print(self.__array)


s = Stack()
string = "the coder school"
for c in string:
    s.push(c)

for i in range(len(string)):
    print(s.peek(), end="")
    s.pop()


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




