def rounded_avg(n, m):
    if m < n:
        return -1
    summation = 0
    for i in range(n, m + 1):
        summation = summation + i
    count = m - n + 1
    average = summation / count
    rounded_average = round(average)
    binary_string = bin(rounded_average)
    return binary_string