# 791. Custom Sort String


def custom_sort_string(s, t):
    maps = {}
    for i in t:
        if i not in maps:
            maps[i] = 1
        else:
            maps[i] += 1
    inside = ''
    for j in range(len(s)):
        if s[j] in T:
            inside += s[j] * maps[s[j]]
            maps[s[j]] = 0
    for k in maps:
        if maps[k] != 0:
            inside += k * maps[k]
    return inside
