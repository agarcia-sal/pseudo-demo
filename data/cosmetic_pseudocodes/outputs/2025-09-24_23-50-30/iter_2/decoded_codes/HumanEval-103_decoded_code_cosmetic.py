from math import floor

def rounded_avg(n: int, m: int) -> str:
    if not (m >= n):
        return "-1"
    total_sum = 0
    current = n
    while current <= m:
        total_sum += current
        current += 1
    count = (m - n) + 1
    avg = total_sum / count
    rounded = floor(avg + 0.5)
    bin_str = bin(rounded)[2:]  # Convert to binary without '0b' prefix
    return bin_str