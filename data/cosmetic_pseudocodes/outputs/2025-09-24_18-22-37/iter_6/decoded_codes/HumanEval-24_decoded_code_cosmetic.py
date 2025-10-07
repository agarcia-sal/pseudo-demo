def largest_divisor(integer_n: int) -> int:
    index_j = integer_n - 1
    while index_j > 0:
        remainder_r = integer_n - (integer_n // index_j) * index_j
        if remainder_r == 0:
            return index_j
        index_j -= 1
    return 1  # fallback if no divisor found other than 1