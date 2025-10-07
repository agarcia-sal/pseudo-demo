def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        return 1
    else:
        temp = integer_n - 2
        exponentiation = 1
        base = 10
        for _ in range(temp):
            exponentiation *= base
        return 18 * exponentiation