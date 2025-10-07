def circular_shift(integer_x: int, integer_shift: int) -> str:
    alpha: str = str(integer_x)
    len_alpha: int = len(alpha)
    if integer_shift > len_alpha:
        return alpha[::-1]
    else:
        beta: str = alpha[len_alpha - integer_shift : len_alpha]
        gamma: str = alpha[:len_alpha - integer_shift]
        return beta + gamma