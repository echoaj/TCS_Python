

'''
Create a recursive algorithm that returns True or False
if there exists a combination of x and/or y numbers that
add up to a limit.
'''


def addup(limit, x, y, total):
    if total == limit:
        return True
    if total > limit:
        return False

    r1 = addup(limit, x, y, total+x)
    r2 = addup(limit, x, y, total+y)
    return r1 or r2


print(addup(11, 2, 3, 0))   # True (2+2+2+2+3 = 11)
print(addup(10, 5, 3, 0))   # True (5+5 = 10)
print(addup(8, 3, 6, 0))    # False (No combination exists)
print(addup(19, 5, 7, 0))   # True (5+7+7 = 19)
print(addup(13, 4, 2, 0))   # False (No combination exists)



























# actualHeight = 0
#
# jheight = 5
# velocity = jheight
#
# gravity = 1
#
# while velocity > 0:
#     actualHeight += velocity #(velocity * gravity) + (gravity / velocity)
#     velocity -= gravity
#     print(actualHeight)





'''
print()
print()
import asyncio

# operator overloading
# decorators
# iterables vs iterators, generators
# design patterns
# dependency injection

class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.money = amount

    def display(self):
        print(self.name, self.money)

    def __add__(self, other):
        return self.money + other.money



savings = BankAccount("Alex", 50000)
checking = BankAccount("Josh", 90000)
print(savings + checking)




from time import *

# async def fun():
#     print("hello world")
#     await asyncio.sleep(5)
#     print("done")
#
# asyncio.run(fun())


print()
print()


grassID = 2
grassDur = 3    # takes 3 hits

stoneID = 3
stoneDur = 5    # takes 3 hits

blocks = [0,3,3,1,2,1,2,0]    # block type
hitCount = [0, 0, 0]     # [block_type, hitcount]

while True:
    print(hitCount)
    i = int(input("Pick a block: "))
    result = blocks[i]
    print("result: " + str(result))
    if result == hitCount[0]:
        # increase hit count
        hitCount[1] += 1
        if hitCount[0] == grassID and hitCount[1] >= grassDur:
            print("grass destoryed")
            hitCount = [0, 0]
        if hitCount[0] == stoneID and hitCount[1] >= stoneDur:
            print("stone destroyed")
            hitCount = [0, 0]
    else:
        hitCount = [result, 1]

'''