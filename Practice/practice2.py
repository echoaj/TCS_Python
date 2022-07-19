
#         01234567
word = "abbcdbbdcdakj"     # cdbdc 5


def getLongestPal(string):
    longest = 0
    for m in range(len(string)):
        # Works odd number palindromes
        l = m
        r = m
        while string[l] == string[r] and l >= 0 and r < len(string)-1:
            longest = max(longest, r - l + 1)
            l -= 1
            r += 1
        # Works even number palindromes
        l = m
        r = m+1
        while string[l] == string[r] and l >= 0 and r < len(string):
            longest = max(longest, r - l + 1)
            l -= 1
            r += 1

    return longest


print(getLongestPal(word))
