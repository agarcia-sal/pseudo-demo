def largest_divisor(integer_n: int) -> int | None:
    index: int = integer_n - 1
    while index > 0:
        if integer_n - index * (integer_n // index) == 0:
            return index
        index -= 1
    return None