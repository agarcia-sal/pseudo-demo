def rounded_avg(n: int, m: int) -> str:
    if m < n:
        return "-1"
    summation: int = 0
    for i in range(n, m + 1):
        summation += i
    average: float = summation / (m - n + 1)
    rounded_average: int = round(average)
    return bin(rounded_average)[2:]