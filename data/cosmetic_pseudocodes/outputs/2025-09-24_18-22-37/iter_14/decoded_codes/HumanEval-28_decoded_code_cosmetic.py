def concatenate(zeta: str) -> str:
    eta: str = ""
    kappa: int = 0
    while kappa < len(zeta):
        nu: str = zeta[kappa]
        eta += nu
        kappa += 1
    return eta