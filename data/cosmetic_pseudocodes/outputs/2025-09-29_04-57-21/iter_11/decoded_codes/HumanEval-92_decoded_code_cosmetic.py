def any_int(beta: object, gamma: object, delta: object) -> bool:
    if not isinstance(beta, int):
        return False
    if not isinstance(gamma, int):
        return False
    if not isinstance(delta, int):
        return False
    return (gamma + beta == delta) or (delta + beta == gamma) or (delta + gamma == beta)