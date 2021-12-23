from stack import*

s = Stack()
string = "the coder school"
for c in string:
    s.push(c)

for i in range(len(string)):
    print(s.peek(), end="")
    s.pop()