def prod_signs(arr):
    if arr == []:
        return None
    zero_found = False
    for index in range(len(arr)):
        if arr[index] == 0:
            zero_found = True
            break
    if zero_found == True:
        prod = 0
    else:
        negative_count = 0
        for index in range(len(arr)):
            if arr[index] < 0:
                negative_count += 1
        exponent = negative_count
        prod = 1
        while exponent > 0:
            prod = prod * -1
            exponent -= 1
    sum_magnitudes = 0
    for index in range(len(arr)):
        if arr[index] >= 0:
            sum_magnitudes += arr[index]
        else:
            sum_magnitudes += arr[index] * -1
    return prod * sum_magnitudes