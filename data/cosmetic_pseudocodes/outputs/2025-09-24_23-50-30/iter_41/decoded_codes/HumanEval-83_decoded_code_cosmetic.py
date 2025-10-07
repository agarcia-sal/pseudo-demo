def starts_one_ends(integer_n: int) -> int:
    if integer_n == 1:
        return 1
    else:
        alpha: int = 10
        beta: int = integer_n - 2
        gamma: int = 1
        while beta > 0:
            gamma *= alpha
            beta -= 1
        return 18 * gamma