# 1365. How Many Numbers Are Smaller Than the Current Number


# 1
def smaller_numbers_than_current(nums):
    temp = sorted(nums)
    maps = {}
    result = []
    for i in range(len(nums)):
        if temp[i] not in maps:
            maps[temp[i]] = i
    for j in nums:
        result.append(maps[j])
    return result


# quick sort ?
