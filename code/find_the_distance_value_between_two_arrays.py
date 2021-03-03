# 1385. Find the Distance Value Between Two Arrays


def find_the_distance_value(arr1, arr2, d):
    result = 0
    for i in arr1:
        check = True
        for y in arr2:
            if abs(i-y) <= d:
                check = False
                break
        if check:
            result += 1
    return result
