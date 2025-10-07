def rounded_avg(alpha: int, beta: int) -> str:
    if beta < alpha:
        return "-1"
    delta = alpha
    epsilon = 0
    while delta <= beta:
        epsilon += delta
        delta += 1
    zeta = beta - alpha + 1
    eta = epsilon / zeta
    theta = round(eta)
    iota = bin(theta)[2:]
    return iota