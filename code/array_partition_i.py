# 561. Array Partition I


def array_pair_sum(nums):
    nums.sort()
    sums = 0
    for i in range(0, len(nums), 2):
        sums += nums[i]
    return sums
