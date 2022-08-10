

# dictionary with key value pairs
combos = {}


# Given a list of numbers find all combinations where a+b=c+d
nums = [1, 7, 3, 8, 12, 4, 2, 0, 5, 10]
# 7 + 3 = 0 + 10
# 7 + 1 = 8 + 0
# 8 + 3 = 10 + 1

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        key = nums[i] + nums[j]
        if key in combos:
            combos[key].append((nums[i], nums[j]))
        else:
            combos[key] = [(nums[i], nums[j])]


for key in combos:
    print(key, combos[key])

