def minSubArraySum(nums):
    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if s < 0:
            s = 0
        if s > max_sum:
            max_sum = s
    if max_sum == 0:
        max_neg = -nums[0]
        for i in nums[1:]:
            neg_i = -i
            if neg_i > max_neg:
                max_neg = neg_i
        max_sum = max_neg
    min_sum = -max_sum
    return min_sum