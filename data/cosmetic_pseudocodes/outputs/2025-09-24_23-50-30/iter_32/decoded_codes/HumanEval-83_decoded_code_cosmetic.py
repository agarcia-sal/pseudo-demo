def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        return 1
    else:
        var_x = 1
        for _ in range(1, integer_n - 1):
            var_x *= 10
        return 18 * var_x