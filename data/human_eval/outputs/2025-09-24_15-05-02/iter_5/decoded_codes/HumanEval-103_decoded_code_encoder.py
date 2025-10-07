def rounded_avg(n, m):
    if m < n:
        return -1

    total_sum = 0
    for i in range(n, m + 1):
        total_sum += i

    average = total_sum / (m - n + 1)
    rounded_average = round(average)
    binary_result = bin(rounded_average)
    return binary_result