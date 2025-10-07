def minSubArraySum(nums):
    max_sum = s = 0
    for num in nums:
        s += -num
        if s < 0:
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    return -max_sum