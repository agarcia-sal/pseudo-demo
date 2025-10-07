def choose_num(a: int, b: int) -> int:
    if not (a <= b):
        return -1

    remainder_is_zero = b % 2
    if remainder_is_zero == 0:
        return b

    if a == b:
        return -1

    adjusted_value = b - 1
    return adjusted_value