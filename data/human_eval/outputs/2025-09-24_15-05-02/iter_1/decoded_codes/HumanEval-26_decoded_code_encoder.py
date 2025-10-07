def remove_duplicates(nums):
    from collections import Counter
    c = Counter(nums)
    return [n for n in nums if c[n] <= 1]