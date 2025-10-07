def rounded_avg(n: int, m: int) -> str:
    if m < n:
        return -1

    summation = 0
    index = n
    while index <= m:
        summation += index
        index += 1

    count = m - n + 1
    average = summation / count
    rounded_value = round(average)
    binary_representation = bin(rounded_value)
    return binary_representation