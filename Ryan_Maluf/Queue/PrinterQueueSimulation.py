
from time import*
from threading import*
from Queue import*
from random import*
from time import *


class Person:

    # ANSI CODE
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    END = "\033[0m"
    BOLD = "\033[1m"

    def __init__(self, ID):
        self.ID  = ID
        self.pages = randint(1,25)
        self.print_time = self.pages / 10
        self.total_time = 0

    def status(self):
        print(self.GREEN + self.BOLD + f"Person {self.ID} | Pages {self.pages} | Print Time {self.print_time} | Total Time {round(self.total_time,1)}" + self.END)

    def finish(self):
        print(self.BLUE + self.BOLD + f"Person {self.ID} finished" + self.END)


def enqueue():
    global x, total
    while True:
        p = Person(x)
        total += p.print_time
        p.total_time += total
        p.status()
        q.push(p)
        x += 1
        sleep(0.5)


def dequeue():
    global total
    while True:
        if not q.is_empty():
            p = q.peek()
            sleep(p.print_time)
            total -= p.print_time
            p.finish()
            q.pop()


q = Queue()
x = 1
total = 0

t1 = Thread(target=enqueue)
t2 = Thread(target=dequeue)

t1.start()
t2.start()

t1.join()
t2.join()
