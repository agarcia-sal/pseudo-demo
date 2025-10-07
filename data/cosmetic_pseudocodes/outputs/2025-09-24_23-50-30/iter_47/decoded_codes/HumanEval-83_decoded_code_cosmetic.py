def starts_one_ends(integer_n: int) -> int:
    integer_x = integer_n
    if integer_x == 1:
        return 1
    else:
        integer_y = integer_x - 2
        integer_z = 10
        integer_w = 1
        for _ in range(integer_y):
            integer_w *= integer_z
        return 18 * integer_w