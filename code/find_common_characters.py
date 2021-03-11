# 1002. Find Common Characters


def common_chars(A):
    res = []
    target = []
    for a in A:
        for b in a:
            if b not in target:
                target.append(b)
    maps = {}
    for i in target:
        buffer = []
        for j in A:
            if i in j:
                maps[i] = 0
                for k in j:
                    if i == k:
                        maps[i] += 1
            else:
                maps[i] = 0
            buffer.append(maps[i])
            maps = {}
            if min(buffer):
                res.extend([i] * min(buffer))
            buffer = []
    return res
