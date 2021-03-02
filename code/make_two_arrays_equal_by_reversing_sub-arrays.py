# 1460. Make Two Arrays Equal by Reversing Sub-arrays


def can_be_equal(target, arr):
    target_map = {}
    arr_map = {}
    for i in target:
        if i not in target_map:
            target_map[i] = 0
        else:
            target_map[i] += 1
    for j in arr:
        if j not in arr_map:
            arr_map[j] = 0
        else:
            arr_map[j] += 1
    if target_map == arr_map:
        return True
    return False
