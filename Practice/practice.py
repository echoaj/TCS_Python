

string = "Thanks diane I will order the medicine next week and let you know."
tokens = string.split()
lables = [0] * len(tokens)


print(tokens)
print(lables)





































# start = {
#     "life":(0, 0, "job", "college"),
#     "job":(1, 40000, "career", "keepjob"),
#     "keepjob":(5, 200000, "wife", "single"),
#     "college":(4, -100000, "masters", "career"),
#     "masters":(2, -50000, "PHD", "goodcareer"),
#     "career":(5, 10000, "wife", "single"),
#     "goodcareer":(5, 20000, "wife", "sngle"),
#     "PHD":(4, -100000, "greatcareer", "greatcareer"),
#     "single":(7, 0, "end", "end"),
#     "greatcareer":(5, 500000, "wife", "single"),
#     "wife":(7, 200000, "kids", "end"),
#     "kids":(1, 14000, "end", "end"),
#     "end":()
# }
#
# a1 = [5,6,3]
# a2 = [8,8,5]
# a = [*a1, *a2]
# print(a)
#
# g, *u = [5,6,3,3,2]
# print(g, u)
#
# money = 0
# time = 0
#
# status = None
# tuple = start["life"]
#
#
# while(tuple):
#     years, cash, choice1, choice2 = tuple
#     money += cash
#     time += years
#
#     status = f'Money {money}\t\tTime {time}\nOptions are {choice1} or {choice2}.\nPick 1 or 2: '
#     option = int(input(status)) + 1
#     decision = tuple[option]
#     tuple = start[decision]
#     print()
#
# print("Game Ended")