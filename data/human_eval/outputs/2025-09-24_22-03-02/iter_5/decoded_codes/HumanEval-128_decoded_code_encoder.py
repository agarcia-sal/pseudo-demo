def prod_signs(arr):
    if not arr:
        return None
    if 0 in arr:
        prod = 0
    else:
        negative_count = sum(1 for x in arr if x < 0)
        prod = (-1) ** negative_count
    total_magnitude = sum(abs(x) for x in arr)
    return prod * total_magnitude