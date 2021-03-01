# 1389. Create Target Array in the Given Order


def create_target_array(nums, index):
    result = []
    for i in range(len(nums)):
        result = result[:index[i]] + [nums[i]] + result[index[i:]:]
    return result
