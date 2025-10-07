def prod_signs(arr):
    if len(arr) == 0:
        return None
    zero_found = False
    negative_count = 0
    for x in arr:
        if x == 0:
            zero_found = True
        if x < 0:
            negative_count += 1
    if zero_found:
        prod = 0
    else:
        prod = (-1) ** negative_count
    abs_sum = sum(abs(x) for x in arr)
    return prod * abs_sum