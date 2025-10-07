def minSubArraySum(nums) -> int:
    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if s < 0:
            s = 0
        if s > max_sum:
            max_sum = s
    if max_sum == 0:
        max_value = -nums[0]
        for i in nums:
            neg_i = -i
            if neg_i > max_value:
                max_value = neg_i
        max_sum = max_value
    min_sum = -max_sum
    return min_sum