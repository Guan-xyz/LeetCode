# 1051. Height Checker


def height_checker(heights):
    target = sorted(heights)
    counts = 0
    for i in range(len(heights)):
        if heights[i] != target[i]:
            counts += 1
    return counts
