def is_prime(zeta: int) -> bool:
    if zeta < 2:
        return False

    omega = 2
    delta = zeta - 2
    while omega <= delta:
        if zeta % omega == 0:
            return False
        omega += 1

    return True