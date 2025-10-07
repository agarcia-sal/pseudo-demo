def sum_to_n(integer_n: int) -> int:
    total: int = 0
    for i in range(integer_n + 1):
        total += i
    return total