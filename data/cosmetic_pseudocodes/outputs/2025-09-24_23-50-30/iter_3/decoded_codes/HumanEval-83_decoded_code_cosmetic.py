def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        return 1
    power_val = 1
    for _ in range(1, integer_n - 1):
        power_val *= 10
    return 18 * power_val