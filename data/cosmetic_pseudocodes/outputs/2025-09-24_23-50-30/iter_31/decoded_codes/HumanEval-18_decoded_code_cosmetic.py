def how_many_times(alpha: str, beta: str) -> int:
    delta: int = len(alpha) - len(beta)

    def epsilon(zeta: int, eta: int) -> int:
        if zeta > delta:
            return 0
        if alpha[zeta : zeta + len(beta)] == beta:
            return 1 + epsilon(zeta + 1, eta)
        else:
            return epsilon(zeta + 1, eta)

    return epsilon(0, 0)