# Leetcode 1 Two Sum


"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example 1:
Input nums = [2, 7, 11, 15], target = 9,
Output: [0, 1]
Explanation: The sum of nums[0] and nums[1] is 9 we return [0, 1].

Example 2:
Input nums = [3, 2, 4], target = 6,
Output: [1, 2]
"""

pairs = {}

nums = [-4,6,2,3,5,6,3]
target = 9


output = []

for i in range(len(nums)):
    num = nums[i]
    if num in pairs:
        output.append(pairs[num])
        output.append(i)
        break
    else:
        compilment = target - num
        pairs[compilment] = i

print(output)




