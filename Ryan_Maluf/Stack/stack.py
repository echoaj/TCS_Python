
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
