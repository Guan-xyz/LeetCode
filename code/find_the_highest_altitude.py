# 1732. Find the Highest Altitude


def largest_altitude(gain):
    nums = 0
    altitude = 0
    for i in range(len(gain)):
        nums += gain[i]
        if altitude < nums:
            altitude = nums
    return altitude
