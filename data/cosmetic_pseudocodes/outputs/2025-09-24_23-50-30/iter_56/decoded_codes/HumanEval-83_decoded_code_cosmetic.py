def starts_one_ends(integer_lambda: int) -> int:
    if integer_lambda == 1:
        return 1

    integer_omega: int = 10
    integer_sigma: int = integer_lambda - 2
    integer_alpha: int = 1

    for _ in range(1, integer_sigma + 1):
        integer_alpha *= integer_omega

    return 18 * integer_alpha