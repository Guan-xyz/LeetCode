# 1636. Sort Array by Increasing Frequency


def frequency_sort(nums):
    maps = {}
    for i in nums:
        if i not in maps:
            maps[i] = 1
        else:
            maps[i] += 1
    nums.sort(key=lambda x: (maps[x], -x))
    return nums
