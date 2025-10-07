def rounded_avg(n, m):
    if m < n:
        return -1
    summation = 0
    for i in range(n, m + 1):
        summation += i
    average = summation / (m - n + 1)
    rounded_average = round(average)
    binary_representation = bin(rounded_average)
    return binary_representation