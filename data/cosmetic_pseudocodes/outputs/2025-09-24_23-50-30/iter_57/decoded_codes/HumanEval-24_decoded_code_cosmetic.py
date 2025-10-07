def largest_divisor(integer_n: int) -> int:
    index_j: int = integer_n - 1
    while index_j > 0:
        if integer_n % index_j == 0:
            return index_j
        index_j -= 1
    return 0  # fallback if no divisor found, e.g., integer_n == 1