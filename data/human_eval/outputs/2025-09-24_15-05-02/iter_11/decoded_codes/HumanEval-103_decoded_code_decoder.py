def rounded_avg(n, m):
    if m < n:
        return -1
    summation = 0
    for i in range(n, m + 1):
        summation += i
    average_value = summation / (m - n + 1)
    rounded_average = round(average_value)
    binary_string = bin(rounded_average)
    return binary_string