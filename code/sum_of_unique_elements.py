# 1748. Sum of Unique Elements


def sum_of_unique(nums):
    maps = {}
    for i in nums:
        if i not in maps:
            maps[i] = 0
        else:
            maps[i] += 1
    sums = 0
    for k in maps:
        if maps[k] == 0:
            sums += int(k)
    return sums
