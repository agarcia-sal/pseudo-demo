def starts_one_ends(integer_n: int) -> int:
    integer_x: int = integer_n - 2
    integer_base: int = 10
    integer_power: int = 1

    while True:
        if integer_x < 1:
            break
        integer_power *= integer_base
        integer_x -= 1

    if integer_n == 1:
        return 1
    else:
        return 18 * integer_power