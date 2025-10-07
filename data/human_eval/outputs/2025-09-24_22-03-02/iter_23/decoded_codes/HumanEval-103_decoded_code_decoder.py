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
    rounded_average = round(average)
    result_binary_string = bin(rounded_average)
    return result_binary_string