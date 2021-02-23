# 1431. Kids With the Greatest Number of Candies


def kids_with_candies(candies, extra_candies):
    result = []
    maximum = max(candies)

    for i in candies:
        if i + extra_candies >= maximum:
            result.append(True)
        else:
            result.append(False)
    return result
