def starts_one_ends(alpha: int) -> int:
    beta: int = 1
    if alpha != 1:
        gamma: int = alpha - 2
        delta: int = 10
        epsilon: int = 18
        return epsilon * (delta ** gamma)
    else:
        return beta