def rounded_avg(n, m):
    if m < n:
        return -1
    summation = sum(range(n, m+1))
    average = summation / (m - n + 1)
    rounded_average = round(average)
    return bin(rounded_average)