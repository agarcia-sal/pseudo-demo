def prod_signs(arr):
    if not arr:
        return None
    if 0 in arr:
        product_sign = 0
    else:
        negative_count = sum(1 for x in arr if x < 0)
        product_sign = (-1) ** negative_count
    sum_magnitudes = sum(abs(x) for x in arr)
    return product_sign * sum_magnitudes