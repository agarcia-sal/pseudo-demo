def prod_signs(arr):
    if not arr:
        return None

    if 0 in arr:
        prod = 0
    else:
        negative_count = 0
        for element in arr:
            if element < 0:
                negative_count += 1
        prod = (-1) ** negative_count

    total_magnitude = 0
    for element in arr:
        total_magnitude += abs(element)

    return prod * total_magnitude