def custom_function(m, n):
    if m < n:
        return -1
    total = sum(i for i in range(n, m + 1))
    avg = round(total / (m - n + 1))
    return bin(avg)