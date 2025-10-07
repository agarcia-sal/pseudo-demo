def process_range(n, m):
    if n > m:
        return -1
    total_sum = sum(range(n, m + 1))
    avg = round(total_sum / (m - n + 1))
    return bin(avg)