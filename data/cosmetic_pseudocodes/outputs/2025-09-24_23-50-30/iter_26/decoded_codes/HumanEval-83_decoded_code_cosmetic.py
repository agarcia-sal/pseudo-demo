def starts_one_ends(integer_alpha: int) -> int:
    if integer_alpha == 1:
        return 1
    else:
        beta: int = 10
        gamma: int = integer_alpha - 2
        delta: int = 1
        for _ in range(gamma):
            delta *= beta
        return 18 * delta