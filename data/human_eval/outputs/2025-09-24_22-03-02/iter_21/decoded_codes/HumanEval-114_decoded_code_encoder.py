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
        max_candidate = -nums[0]
        index = 1
        while index < len(nums):
            if -nums[index] > max_candidate:
                max_candidate = -nums[index]
            index += 1
        max_sum = max_candidate
    min_sum = -max_sum
    return min_sum