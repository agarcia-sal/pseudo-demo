def largest_divisor(integer_n: int) -> int | None:
    index_j: int = integer_n - 1
    while index_j > 0:
        if integer_n % index_j == 0:
            return index_j
        index_j -= 1
    return None