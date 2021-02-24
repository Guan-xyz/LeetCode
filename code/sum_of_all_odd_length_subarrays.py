# 1588. Sum of All Odd Length Subarrays


def sum_odd_length_subarrays(arr):
    sums = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if len(arr[i:j]) % 2 != 0:
                sums += sum(arr[i:j])
    return sums
