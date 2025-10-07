def mean_absolute_deviation(nums):
    mean = sum(nums) / len(nums)
    return sum(abs(x - mean) for x in nums) / len(nums)