def rounded_avg(n: int, m: int) -> str:
    if m < n:
        return -1
    summation = sum(range(n, m + 1))
    average = summation / (m - n + 1)
    rounded_average = round(average)
    binary_representation = bin(rounded_average)[2:]
    return binary_representation