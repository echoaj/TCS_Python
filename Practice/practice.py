# Parent class, Base class, Super class
class Employee:
    def __init__(self, fn, ln, ag, em, ssn):
        self.firstName = fn
        self.lastName = ln
        self.age = ag
        self.email = em
        self.SSN = ssn

    def display(self):
        print()
        print(self.firstName, self.lastName)
        print(f"AGE: {self.age} Email: {self.email}")
        print(f"SSN: {self.SSN}")


# Sub class, Child class
class Manager(Employee):
    def __init__(self, fn, ln, ag, em, ssn, dep, rf):
        super(Manager, self).__init__(fn, ln, ag, em, ssn)
        self.department = dep
        self.resp_for = rf

    # overriding
    def display(self):
        super(Manager, self).display()
        print(self.department, self.resp_for)
        print()


emp = Employee("Alex", "Joslin", 26, "aj@gmail.com", 123456789)
emp.display()

mng = Manager("Lisa", "Janis", 56, "aj@gmail.com", 123456789, "software", 15)
mng.display()   # polymorphism