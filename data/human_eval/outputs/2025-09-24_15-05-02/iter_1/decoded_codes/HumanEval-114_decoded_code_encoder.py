def minSubArraySum(nums):
    max_s, s = 0, 0
    for n in nums:
        s += -n
        if s < 0:
            s = 0
        max_s = max(s, max_s)
    if max_s == 0:
        max_s = max(-i for i in nums)
    return -max_s