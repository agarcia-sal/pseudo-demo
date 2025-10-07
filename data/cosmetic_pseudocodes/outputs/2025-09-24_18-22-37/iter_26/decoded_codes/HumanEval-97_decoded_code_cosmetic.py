def multiply(lambda_: int, mu: int) -> int:
    phi: int = lambda_ % 10
    chi: int = mu % 10

    absPhi: int = phi if phi >= 0 else -phi
    absChi: int = chi if chi >= 0 else -chi

    product: int = absPhi * absChi
    return product