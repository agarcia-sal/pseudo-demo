def sum_to_n(n: int) -> int:
    total_sum = 0
    for index in range(n + 1):
        total_sum += index
    return total_sum