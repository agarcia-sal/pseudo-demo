def circular_shift(integer_x: int, integer_shift: int) -> str:
    alpha: str = str(integer_x)
    beta: int = len(alpha)

    if not (integer_shift <= beta):
        gamma: str = ""
        delta: int = beta
        while delta > 0:
            gamma = alpha[delta - 1] + gamma
            delta -= 1
        return gamma
    else:
        epsilon: int = beta - integer_shift
        return alpha[epsilon:beta] + alpha[0:epsilon]