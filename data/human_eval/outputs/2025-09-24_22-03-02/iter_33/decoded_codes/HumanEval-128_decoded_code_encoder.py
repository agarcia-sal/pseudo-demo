def prod_signs(arr):
    if len(arr) == 0:
        return None

    zero_found = False
    negative_count = 0

    for num in arr:
        if num == 0:
            zero_found = True
        if num < 0:
            negative_count += 1

    if zero_found:
        prod = 0
    else:
        prod = (-1) ** negative_count

    total_abs_sum = sum(abs(num) for num in arr)

    return prod * total_abs_sum