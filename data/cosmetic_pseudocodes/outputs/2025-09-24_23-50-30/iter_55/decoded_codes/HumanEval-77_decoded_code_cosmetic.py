def iscube(integer_alpha: int) -> bool:
    integer_beta: int = abs(integer_alpha)
    integer_gamma: int = round(integer_beta ** (1 / 3))
    integer_delta: int = integer_gamma ** 3
    return integer_delta == integer_beta