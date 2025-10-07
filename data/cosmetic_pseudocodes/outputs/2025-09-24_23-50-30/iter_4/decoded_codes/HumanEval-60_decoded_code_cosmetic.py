def sum_to_n(integer_n: int) -> int:
    if integer_n < 0:
        return 0
    return sum(x for x in range(integer_n + 1))