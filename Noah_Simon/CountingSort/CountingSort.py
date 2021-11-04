

def counting_sort(array):
    sorted_list = [0] * len(array)
    occurrences = [0] * (max(array) + 1)

    # Occurrences
    for i in array:
        occurrences[i] += 1

    # Find Sums
    sums = [occurrences[0]]
    for i in range(1, len(occurrences)):
        sums.append(occurrences[i]+ sums[i-1])

    # Shift Right
    shifted = [0]
    sums.pop()
    shifted += sums

    # Sort
    for i in array:
        index = shifted[i]
        shifted[i] += 1
        sorted_list[index] = i
    return sorted_list


nums = [3,5,2,2,1,2]
nums = counting_sort(nums)
print(nums)