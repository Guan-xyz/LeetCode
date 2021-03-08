# 771. Jewels and Stones


def num_jewels_in_stones(jewels, stones):
    counts = 0
    for i in stones:
        if i in jewels:
            counts += 1
    return counts
