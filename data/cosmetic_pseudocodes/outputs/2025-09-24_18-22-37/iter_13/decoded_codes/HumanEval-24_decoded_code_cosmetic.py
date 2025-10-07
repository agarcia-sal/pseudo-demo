def largest_divisor(integer_n: int) -> int:
    iterator_index = integer_n - 1
    while iterator_index > 0:
        remainder = integer_n - (integer_n // iterator_index) * iterator_index
        if remainder == 0:
            return iterator_index
        iterator_index -= 1
    # If no divisor found (only when integer_n <= 1), return 1 as fallback
    return 1