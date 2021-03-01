# 1534. Count Good Triplets


def count_good_triplets(arr, a, b, c):
    counts = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if abs(arr[i] - arr[j]) <= a:
                for k in range(j+1, len(arr)):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        counts += 1
    return counts
