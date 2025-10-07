def rounded_avg(n: int, m: int) -> str:
    if m < n:
        return -1
    length = m - n + 1
    summation = sum(n + i for i in range(length))
    average = summation / length
    rounded_average = round(average)
    binary_representation = bin(rounded_average)
    return binary_representation