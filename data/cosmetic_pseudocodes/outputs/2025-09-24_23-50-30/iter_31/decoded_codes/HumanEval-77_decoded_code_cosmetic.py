def iscube(delta: int) -> bool:
    omega = -delta if delta < 0 else delta
    psi = round(omega ** (1 / 3))
    chi = psi * psi * psi
    return chi == omega