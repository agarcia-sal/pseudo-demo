def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        return 1
    else:
        temp_var = integer_n - 2
        exponent_result = 1
        counter = 0
        while counter < temp_var:
            exponent_result *= 10
            counter += 1
        return 18 * exponent_result