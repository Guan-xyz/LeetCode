# 1351. Count Negative Numbers in a Sorted Matrix


def count_negatives(grid):
    counts = 0
    for i in grid:
        for j in i:
            if j < 0:
                counts += 1
    return counts
