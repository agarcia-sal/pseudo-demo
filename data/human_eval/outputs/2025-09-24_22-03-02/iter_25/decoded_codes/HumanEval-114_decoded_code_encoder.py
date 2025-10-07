def minSubArraySum(nums):
    max_sum = 0
    s = 0
    length_nums = len(nums)
    for index in range(length_nums):
        num = nums[index]
        s += -num
        if s < 0:
            s = 0
        if s > max_sum:
            max_sum = s
    if max_sum == 0:
        max_neg = -nums[0]
        for index in range(1, length_nums):
            if -nums[index] > max_neg:
                max_neg = -nums[index]
        max_sum = max_neg
    min_sum = -max_sum
    return min_sum