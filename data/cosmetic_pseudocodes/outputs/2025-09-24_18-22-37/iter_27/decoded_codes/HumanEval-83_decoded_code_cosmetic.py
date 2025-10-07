def starts_one_ends(beta: int) -> int:
    if beta == 1:
        return 1
    else:
        gamma: int = beta - 2
        delta: int = 1
        epsilon: int = 10
        zeta: int = 1
        while zeta <= gamma:
            delta *= epsilon
            zeta += 1
        eta: int = 18
        theta: int = eta * delta
        return theta