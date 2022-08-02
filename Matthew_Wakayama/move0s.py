# Move all zeros to the end of the array
# All numbers in the array are unique


array = [1, 2, 0, 4, 0, 0, 7, 0, 9]         # [1, 2, 4, 7, 9, 0, 0, 0, 0]

# Steps:
# 1) Set left and right pointer to 0
# 2) If the right pointer is at 0 only move the right.  Otherwise, move both right and left
# 3) When the right pointer find a non 0 switch left and right pointer.

l = 0
r = 0
while r < len(array):
    if array[r] == 0:
        r += 1
    else:
        array[l], array[r] = array[r], array[l]
        r += 1
        l += 1

print(array)