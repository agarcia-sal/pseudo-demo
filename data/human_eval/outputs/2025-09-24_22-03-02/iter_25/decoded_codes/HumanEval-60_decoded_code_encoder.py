def sum_to_n(n: int) -> int:
    total = 0
    i = 0
    while i <= n:
        total += i
        i += 1
    return total