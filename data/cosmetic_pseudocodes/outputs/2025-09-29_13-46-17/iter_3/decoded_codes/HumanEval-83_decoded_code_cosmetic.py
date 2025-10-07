def starts_one_ends(integer_n: int) -> int:
    if integer_n != 1:
        power_result = 1
        count = integer_n - 2
        while count > 0:
            power_result *= 10
            count -= 1
        return 18 * power_result
    return 1