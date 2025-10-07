def is_prime(beta: int) -> bool:
    if beta < 2:
        return False

    def recur_gamma(epsilon: int, zeta: int) -> bool:
        if zeta > epsilon - 2:
            return True
        if epsilon % zeta == 0:
            return False
        return recur_gamma(epsilon, zeta + 1)

    return recur_gamma(beta, 2)