def sum_to_n(kappa: int) -> int:
    delta = 0
    theta = 0
    while theta <= kappa:
        xi = delta + theta
        delta = xi
        theta += 1
    return delta