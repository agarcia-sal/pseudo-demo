def starts_one_ends(number_k: int) -> int:
    if number_k == 1:
        return 1
    exponent_value = number_k - 2
    result_value = 10 ** exponent_value
    return 18 * result_value