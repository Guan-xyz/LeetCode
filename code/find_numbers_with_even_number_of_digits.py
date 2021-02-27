# 1295. Find Numbers with Even Number of Digits


def find_numbers(nums):
    counts = 0
    for i in nums:
        n = 0
        while i:
            i //= 10
            n += 1
        if n % 2 == 0:
            counts += 1
        n = 0
    return counts
