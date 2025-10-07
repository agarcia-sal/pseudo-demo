def rounded_avg(n: int, m: int) -> str:
    if m < n:
        return -1
    summation = 0
    for i in range(n, m + 1):
        summation += i
    count = m - n + 1
    average = summation / count
    rounded_average = round(average)
    binary_representation = bin(rounded_average)
    return binary_representation