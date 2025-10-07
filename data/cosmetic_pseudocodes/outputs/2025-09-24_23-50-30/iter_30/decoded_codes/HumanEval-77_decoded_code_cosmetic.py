def iscube(delta: int) -> bool:
    omega = abs(delta)
    psi = round(omega ** (1 / 3))
    chi = psi * psi * psi
    if chi == omega:
        return True
    return False