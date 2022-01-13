



class BankAccount:
    def __init__(self,name, money):
        self.name = name
        self.money = money

    def display(self):
        print(f"{self.name} has {self.money} in their account")

    def __add__(self, other):
        ba = BankAccount(self.name, self.money + other.money)
        return ba

    def __sub__(self, other):
        ba = BankAccount(self.name, self.money - other.money)
        return ba

    def __mul__(self, other):
        ba = BankAccount(self.name, self.money * other.money)
        return ba

    def __str__(self):
        return "Bank Account has " + str(self.money)


savings = BankAccount("Alex", 50000)
checking = BankAccount("Alex", 24500)
result_account = savings + checking
# result_account.display()

print(result_account)



'''
Create a recursive algorithm that returns True or False
if there exists a combination of x and/or y numbers that
add up to a limit.
'''
# print(True or False)
#
# def addup(limit, x, y, total):
#     if total == limit:
#         return True
#     if total > limit:
#         return False
#
#     r1 = addup(limit, x, y, total+x)
#     r2 = addup(limit, x, y, total+y)
#     return r1 or r2
#
#
# print(addup(11, 2, 3, 0))   # True (2+2+2+2+3 = 11)
# print(addup(10, 5, 3, 0))   # True (5+5 = 10)
# print(addup(8, 3, 6, 0))    # False (No combination exists)
# print(addup(19, 5, 7, 0))   # True (5+7+7 = 19)
# print(addup(13, 4, 2, 0))   # False (No combination exists)







# def countX(string, i, count):
#     if i == len(string)-1:
#         return count
#     if string[i] == "x":
#         count += 1
#     return countX(string, i+1, count)
#
# print(countX("abxcdxxr", 0, 0))
#
# # what are all the compinations of numbers that multiply to limit
# def multToNum(limit, num, pairs):
#     if num == limit:
#         return pairs
#     if limit % num == 0:
#         pairs.append([num, limit/num])
#     return multToNum(limit, num+1, pairs)
#
# print(multToNum(99, 1, []))
