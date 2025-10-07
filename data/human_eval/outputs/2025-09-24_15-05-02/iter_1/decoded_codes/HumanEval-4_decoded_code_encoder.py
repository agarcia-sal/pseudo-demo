def mean_absolute_deviation(nums):
    mu = sum(nums) / len(nums)
    return sum(abs(x - mu) for x in nums) / len(nums)