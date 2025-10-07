def rounded_avg(n: int, m: int) -> str:
    if m < n:
        return -1
    summation = sum(range(n, m + 1))
    average = summation / (m - n + 1)
    rounded_value = round(average)
    binary_string = bin(rounded_value)[2:]
    return binary_string