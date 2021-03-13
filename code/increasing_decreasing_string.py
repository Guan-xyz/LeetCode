# 1502. Can Make Arithmetic Progression From Sequence


def can_make_arithmetic_progression(arr):
    arr.sort()
    target = arr[1] - arr[0]
    for i in range(1, len(arr)):
        if (arr[i] - arr[i-1]) != target:
            return False
    return True
