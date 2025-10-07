def prod_signs(arr: list[int]) -> int | None:
    if arr == []:
        return None
    contains_zero = False
    negative_count = 0
    index = 0
    while index < len(arr):
        if arr[index] == 0:
            contains_zero = True
        elif arr[index] < 0:
            negative_count += 1
        index += 1
    if contains_zero:
        prod = 0
    else:
        prod = 1
        exponent = negative_count
        while exponent > 0:
            prod *= -1
            exponent -= 1
    sum_magnitudes = 0
    index = 0
    while index < len(arr):
        if arr[index] >= 0:
            sum_magnitudes += arr[index]
        else:
            sum_magnitudes += arr[index] * -1
        index += 1
    return prod * sum_magnitudes