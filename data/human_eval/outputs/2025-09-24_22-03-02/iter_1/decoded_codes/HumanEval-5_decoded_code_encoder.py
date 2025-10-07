def intersperse(nums, delim):
    if not nums:
        return []
    return [nums[i] + [delim] for i in range(len(nums) - 1)] + [nums[-1]]