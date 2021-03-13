# 1528. Shuffle String


def restore_string(s, indices):
    res = [''] * len(s)
    for i in range(len(s)):
        res[indices[i]] = s[i]
    return ''.join(res)
