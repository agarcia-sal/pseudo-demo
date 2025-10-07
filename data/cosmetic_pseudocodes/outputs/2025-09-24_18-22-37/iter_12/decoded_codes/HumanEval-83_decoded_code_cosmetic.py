def starts_one_ends(value_m: int) -> int:
    if value_m != 1:
        temp_a: int = 10
        temp_b: int = value_m - 2
        temp_c: int = 1
        for _ in range(1, temp_b + 1):
            temp_c *= temp_a
        temp_d: int = 18 * temp_c
        return temp_d
    else:
        return 1