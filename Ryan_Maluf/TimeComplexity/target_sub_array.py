

nums = [1, 2, 3, 4, 5]
target = 9


def sub_array_sum(array, target):
    l = 0
    r = 1
    total = array[l] + array[r]
    while r < len(array):
        if total == target:
            return True
        elif total < target:
            r += 1
            if r < len(array):
                total += array[r]
        elif total > target:
            total -= array[l]
            l += 1
    return False


print(sub_array_sum(nums, target))