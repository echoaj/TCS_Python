
# Doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, val):
        self.head = Node(val)
        self.tail = self.head

    def append(self, val):
        self.tail.next = Node(val)
        self.tail.next.prev = self.tail
        self.tail = self.tail.next

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, end=" <->")
                temp = temp.next
            print()


dll = DoublyLinkedList(5)
dll.append(10)
dll.append(10)
dll.append(10)
dll.append(10)
dll.display()
