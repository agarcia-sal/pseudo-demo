def normalize(nums):
    min_val = min(nums)
    max_val = max(nums)
    return [(x - min_val) / (max_val - min_val) for x in nums]