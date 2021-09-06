from random import *
import math

money = 0
amount = 1
percentage = 0

for i in range(1000):
    money += randint(1, 8)
    if i % 50 == 0:
        amount += 1

    # percentage = ((1 - i**2 + i**4) / (1 + i**4))

    percentage = 1 - (1 / (amount * (1 - (1/money))))
    print(percentage)

    # 1 / (1 + math.exp(100))