def prod_signs(arr):
    if len(arr) == 0:
        return None
    if 0 in arr:
        prod = 0
    else:
        negative_count = sum(1 for x in arr if x < 0)
        prod = -1 if negative_count % 2 else 1
    sum_magnitudes = sum(abs(x) for x in arr)
    return prod * sum_magnitudes