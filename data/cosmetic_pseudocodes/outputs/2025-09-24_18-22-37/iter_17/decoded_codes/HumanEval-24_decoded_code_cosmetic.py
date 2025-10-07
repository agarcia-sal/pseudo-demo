def largest_divisor(integer_n: int) -> int:
    reversed_index = integer_n - 1
    while reversed_index > 0:
        if integer_n % reversed_index == 0:
            return reversed_index
        reversed_index -= 1
    # No divisor found other than 1 (which will be returned)
    return 1