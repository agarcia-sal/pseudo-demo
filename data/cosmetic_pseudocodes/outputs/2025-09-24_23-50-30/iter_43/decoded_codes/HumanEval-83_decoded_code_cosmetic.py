def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        return 1
    else:
        var_a: int = 10
        var_b: int = integer_n - 2
        var_c: int = 1
        for _ in range(var_b):
            var_c *= var_a
        return 18 * var_c