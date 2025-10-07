def prod_signs(arr):
    if not arr:
        return None
    if 0 in arr:
        p = 0
    else:
        p = (-1) ** sum(x < 0 for x in arr)
    return p * sum(abs(x) for x in arr)