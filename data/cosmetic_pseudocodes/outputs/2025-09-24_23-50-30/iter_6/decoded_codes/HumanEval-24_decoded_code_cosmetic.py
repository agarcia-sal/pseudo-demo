def largest_divisor(integer_n: int) -> int:
    index_var = integer_n - 1
    while index_var > 0:
        if integer_n % index_var == 0:
            return index_var
        index_var -= 1
    # By definition, 1 divides every integer, so this will always return before 0
    return 1