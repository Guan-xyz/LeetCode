# 1680. Concatenation of Consecutive Binary Numbers


def concatenated_binary(n):
    binary_str = ''
    for i in range(1, n+1):
        binary_str += str(bin(i))[2:]
    res = int(binary_str, 2)
    print(res)
    return res % 1000000007
