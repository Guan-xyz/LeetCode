# 1446. Consecutive Characters


def max_power(s):
    count = 0
    max_count = 0
    previous = None
    for i in s:
        if i == previous:
            count += 1
        else:
            previous = i
            count = 1
        max_count = max(max_count, count)
    return max_count
