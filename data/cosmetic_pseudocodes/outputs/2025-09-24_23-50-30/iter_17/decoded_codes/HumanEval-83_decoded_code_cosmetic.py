def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        return 1
    temp_a: int = integer_n - 2
    temp_b: int = 10
    temp_c: int = 1
    while temp_a > 0:
        temp_c *= temp_b
        temp_a -= 1
    return 9 * 2 * temp_c