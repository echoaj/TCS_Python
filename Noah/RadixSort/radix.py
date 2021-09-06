
def counting_sort(array, exp):
    sorted_list = [0] * len(array)
    occurrences = [0] * 10

    # Occurrences
    for num in array:
        digit = (num // exp) % 10
        occurrences[digit] += 1

    # Find Sums
    sums = [occurrences[0]]
    for i in range(1, len(occurrences)):
        sums.append(occurrences[i]+ sums[i-1])

    # Shift Right
    shifted = [0]
    sums.pop()
    shifted += sums

    # Sort
    for num in array:
        digit = (num // exp) % 10
        index = shifted[digit]
        shifted[digit] += 1
        sorted_list[index] = num
    return sorted_list


def RadixSort(array):
    exp = 1
    while max(array) // exp > 0:
        array = counting_sort(array, exp)
        exp *= 10
    return array


nums = [6483, 19, 760, 5, 428, 89]
nums = RadixSort(nums)
print(nums)

### Practice ###
# 6483 // 1 = 6483
# 6483 // 10 = 648
# 6483 // 100 = 64
# 6483 // 1000 = 6
# 6483 // 10000 = 0
