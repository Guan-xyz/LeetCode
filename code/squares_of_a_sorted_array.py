# 977. Squares of a Sorted Array


def sorted_squares(nums):
    a = [i**2 for i in nums]
    a.sort()
    return a
