def prime_length(omega: str) -> bool:
    zeta: int = len(omega)
    if zeta == 0 or zeta == 1:
        return False

    for kappa in range(2, zeta):
        if zeta % kappa == 0:
            return False

    return True