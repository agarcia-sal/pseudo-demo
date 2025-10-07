def rolling_max(nums):
    max_v = None
    res = []
    for n in nums:
        max_v = n if max_v is None else max(max_v, n)
        res.append(max_v)
    return res