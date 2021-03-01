# 1464. Maximum Product of Two Elements in an Array


def max_product(nums):
    a = b = 0
    for i in range(len(nums)):
        if a < nums[i]:
            b = a
            a = nums[i]
        elif nums[i] > b:
            b = nums[i]
    return (a-1) * (b-1)
