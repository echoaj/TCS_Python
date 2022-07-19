

array = [1, 2, 0, 4, 0, 7, 0, 0, 0]         # [1,2,4,7,9,0,0,0,0]

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
