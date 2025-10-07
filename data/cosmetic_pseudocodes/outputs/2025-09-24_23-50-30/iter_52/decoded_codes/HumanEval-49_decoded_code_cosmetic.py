def modp(alpha: int, beta: int) -> int:
    def compute_power(gamma: int, delta: int) -> int:
        if delta == 0:
            return 1
        else:
            return (2 * compute_power(gamma, delta - 1)) % beta
    return compute_power(alpha, alpha)