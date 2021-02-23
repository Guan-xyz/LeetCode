# 1672. Richest Customer Wealth


def maximum_wealth(accounts):
    tmp = 0
    for i in accounts:
        sums = sum(i)
        if tmp < sums:
            tmp = sums
    return tmp
