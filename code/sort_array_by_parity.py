# 905. Sort Array By Parity


def sort_array_by_parity(a):
    odd = []
    even = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd
