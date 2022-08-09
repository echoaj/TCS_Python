

nums = [1,1,1,3,3,4,3,2,4,2]
cache = set()

for num in nums:
    if num in cache:
        print("Duplicate found: {}".format(num))
    else:
        cache.add(num)