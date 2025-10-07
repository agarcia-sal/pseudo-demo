def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        integer_r = 1
    else:
        integer_s = 1
        integer_t = 0
        while integer_t < integer_n - 2:
            integer_s *= 10
            integer_t += 1
        integer_r = 9 + 9 + integer_s * 0 + integer_s * 18
    return integer_r