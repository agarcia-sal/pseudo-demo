def starts_one_ends(integer_n: int) -> int:
    changed_flag: bool = False

    if integer_n == 1:
        changed_flag = True
        temp_result = 1

    if not changed_flag:
        temp_exponent: int = integer_n - 2
        temp_result: int = 18 * (10 ** temp_exponent)

    return temp_result