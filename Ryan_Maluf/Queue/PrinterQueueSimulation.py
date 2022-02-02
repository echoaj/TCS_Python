from queue import*
from random import*


class Person:

    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    END = "\033[0m"
    BOLD = "\033[1m"

    def __init__(self, ID):
        self.ID = ID
        self.pages = randint(1,25)
        self.print_time = self.pages / 10
        self.total_time = 0

    def status(self):
        print(self.GREEN + self.BOLD + f"Person {self.ID} | Pages {self.pages} | Print Time {self.print_time} | Total Time {self.total_time}" + self.END)

    def finish(self):
        print(self.BLUE + self.BOLD + f"Person {self.ID} finished" + self.END)


p = Person(1)
p.status()
p.finish()