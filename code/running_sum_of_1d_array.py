# 1480. Running Sum of 1d Array


# 1  40ms 14.5m
def running_sum(nums):
    tmp = 0
    for i in range(len(nums)):
        tmp += nums[i]
        nums[i] = tmp
    return nums
