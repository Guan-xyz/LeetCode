# 1299. Replace Elements with Greatest Element on Right Side


def replace_elements(arr):
    result = [-1,]
    target = 0
    for i in arr[::-1]:
        if target < i:
            target = i
        result.append(target)
    result.pop()
    return result[::-1]
