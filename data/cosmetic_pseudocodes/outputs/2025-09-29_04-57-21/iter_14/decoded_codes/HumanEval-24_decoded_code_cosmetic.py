def largest_divisor(integer_n: int) -> int | None:
    cursor = integer_n - 1
    while cursor > 0:
        if integer_n % cursor == 0:
            return cursor
        cursor -= 1
    return None