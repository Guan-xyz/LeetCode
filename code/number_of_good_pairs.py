# 1512. Number of Good Pairs


def num_identical_pairs(nums):
    count = 0
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and i < j:
                count += 1
    return count
