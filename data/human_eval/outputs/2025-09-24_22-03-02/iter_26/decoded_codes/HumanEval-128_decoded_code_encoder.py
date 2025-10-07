def prod_signs(arr):
    if len(arr) == 0:
        return None
    zero_found = any(x == 0 for x in arr)
    if zero_found:
        prod = 0
    else:
        negative_count = sum(1 for x in arr if x < 0)
        prod = (-1) ** negative_count
    sum_magnitude = sum(abs(x) for x in arr)
    return prod * sum_magnitude