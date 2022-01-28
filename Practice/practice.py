

def addup(limit, x, y, total):
    if total == limit:
        return True
    elif total > limit:
        return False
    else:
        result1 = addup(limit, x, y, total+x)
        result2 = addup(limit, x, y, total+y)
        return result1 or result2

print(addup(11, 2, 3, 0))
print(addup(11, 2, 3, 0))


def print_nums(i, limit):
    if i > 10:
        return
    else:
        print(i)
        print_nums(i+1, limit)

print_nums(1, 10)


# return a list of all numbers that when multiplied
def mult_combos(limit, x, y, combos):
    # print(x,y)
    if x > limit:
        return combos
    if y > limit:
        return
    if x*y == limit and [x,y] not in combos:
        combos.append([x,y])
        return
    mult_combos(limit, x, y+1, combos)
    return mult_combos(limit, x+1, y, combos)

# print(mult_combos(12, 0, 0, []))

num = 52
strnum = str(num)
char_array = [int(c) for c in strnum]
total = sum(char_array)
print(total)

