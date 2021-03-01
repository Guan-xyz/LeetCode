# 1313. Decompress Run-Length Encoded List


def decompress_rle_list(nums):
    result = []
    for i in range(len(nums) // 2):
        print(nums[2*i], nums[2*i+1])
        result += (nums[2*i] * [nums[2*i+1]])
    return result


print(decompress_rle_list([1, 2, 3, 4]))
