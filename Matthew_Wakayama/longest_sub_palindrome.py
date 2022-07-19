

string = "abbcdbbdcdakj"


def longest_sub_palindrome(string):
    count = 0
    for m in range(len(string)):
        # odd pal
        l = m
        r = m
        while l >= 0 and r < len(string) and string[l] == string[r]:
            count = max(count, r - l + 1)
            l -= 1
            r += 1

        # even pal
        l = m
        r = m+1
        while l >= 0 and r < len(string) and string[l] == string[r]:
            count = max(count, r - l + 1)
            l -= 1
            r += 1
    return count


print(longest_sub_palindrome(string))
