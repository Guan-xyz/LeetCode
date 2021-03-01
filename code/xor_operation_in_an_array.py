# 1486. XOR Operation in an Array


def xor_operation(n, start):
    result = 0
    for i in range(n):
        result ^= (start + 2 * i)
    return result
