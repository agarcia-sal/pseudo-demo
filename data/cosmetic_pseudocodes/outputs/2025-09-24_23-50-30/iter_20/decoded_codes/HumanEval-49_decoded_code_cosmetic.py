def modp(integer_n: int, integer_p: int) -> int:
    alpha: int = 0
    beta: int = 1
    while alpha < integer_n:
        gamma: int = beta * 2
        beta = gamma - (integer_p * (gamma // integer_p))
        alpha += 1
    return beta