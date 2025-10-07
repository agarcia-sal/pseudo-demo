def sum_product(nums):
    sum_ = 0
    prod = 1
    for n in nums:
        sum_ += n
        prod *= n
    return (sum_, prod)