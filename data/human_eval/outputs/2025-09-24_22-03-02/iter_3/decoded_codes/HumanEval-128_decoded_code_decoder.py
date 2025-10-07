def prod_signs(arr):
    if not arr:
        return None
    if 0 in arr:
        prod = 0
    else:
        negative_count = sum(el < 0 for el in arr)
        prod = (-1) ** negative_count
    total_magnitude = sum(abs(el) for el in arr)
    return prod * total_magnitude