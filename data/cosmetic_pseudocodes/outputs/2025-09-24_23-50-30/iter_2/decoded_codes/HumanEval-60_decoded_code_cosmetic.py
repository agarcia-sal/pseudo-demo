def sum_to_n(integer_n: int) -> int:
    if integer_n < 0:
        return 0

    total: int = 0
    current: int = integer_n

    while current >= 0:
        total += current
        current -= 1

    return total