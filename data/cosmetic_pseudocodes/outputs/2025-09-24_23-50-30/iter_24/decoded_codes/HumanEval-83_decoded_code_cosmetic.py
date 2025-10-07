def starts_one_ends(alpha: int) -> int:
    if alpha - 1 == 0:
        return 1
    beta: int = 10
    gamma: int = alpha - 2
    delta: int = beta
    epsilon: int = 1
    while gamma > 0:
        epsilon *= delta
        gamma -= 1
    return epsilon * 18