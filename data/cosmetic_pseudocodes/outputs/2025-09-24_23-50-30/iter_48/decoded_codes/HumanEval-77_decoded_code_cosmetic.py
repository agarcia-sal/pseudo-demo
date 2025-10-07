def iscube(zeta: int) -> bool:
    epsilon: int = (-1 if zeta < 0 else 1)
    mu: float = (zeta * epsilon) ** (1 / 3)
    nu: int = round(mu)
    xi: int = nu * nu * nu
    delta: bool = (xi == zeta * epsilon)
    if delta:
        return True
    else:
        return False