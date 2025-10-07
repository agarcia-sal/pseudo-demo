def minSubArraySum(nums):
    max_sum = 0
    s = 0
    length = len(nums)
    index = 0
    while index < length:
        num = nums[index]
        s += -num
        if s < 0:
            s = 0
        if s > max_sum:
            max_sum = s
        index += 1
    if max_sum == 0:
        max_temp = -nums[0]
        index = 1
        while index < length:
            neg_i = -nums[index]
            if neg_i > max_temp:
                max_temp = neg_i
            index += 1
        max_sum = max_temp
    min_sum = -max_sum
    return min_sum