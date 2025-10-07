def starts_one_ends(integer_r: int) -> int:
    if integer_r == 1:
        return 1
    temp_a: int = 10
    temp_b: int = integer_r
    temp_c: int = temp_b - 2
    temp_d: int = 1
    for _ in range(1, temp_c + 1):
        temp_d *= temp_a
    return 18 * temp_d