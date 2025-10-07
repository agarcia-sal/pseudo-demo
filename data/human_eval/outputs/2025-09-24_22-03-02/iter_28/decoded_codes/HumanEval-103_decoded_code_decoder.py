def rounded_avg(n, m):
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
    binary_result = bin(rounded_average)
    return binary_result