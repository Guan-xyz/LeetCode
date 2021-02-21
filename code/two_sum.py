# 1.Two Sum


def two_sum(nums, target):
    nums_dict = {}
    new_dict = {}
    count = 0

    for i in nums:
        nums_dict[count] = i
        count += 1

    for j, k in nums_dict.items():
        n = target - k
        if n not in new_dict:
            new_dict[k] = j
        else:
            return [new_dict[n], j]

print(two_sum([3, 3], 6))
