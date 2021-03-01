# 1773. Count Items Matching a Rule


def count_matchs(items, rule_key, rule_value):
    maps = {"type": 0, "color": 1, "name": 2}
    counts = 0
    for i in items:
        if i[maps[rule_key]] == rule_value:
            counts += 1
    return counts
