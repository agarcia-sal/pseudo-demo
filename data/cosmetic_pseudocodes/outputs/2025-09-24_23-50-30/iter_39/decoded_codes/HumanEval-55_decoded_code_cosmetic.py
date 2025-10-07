def fib(gamma: int) -> int:
    delta = 0
    epsilon = 1
    zeta = 2
    while zeta <= gamma:
        eta = delta + epsilon
        delta = epsilon
        epsilon = eta
        zeta += 1
    if gamma == 0:
        return delta
    if gamma == 1:
        return epsilon
    return epsilon