def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        return 1
    else:
        temp: int = integer_n - 2
        base: int = 10
        result: int = 18 * (base ** temp)
        return result