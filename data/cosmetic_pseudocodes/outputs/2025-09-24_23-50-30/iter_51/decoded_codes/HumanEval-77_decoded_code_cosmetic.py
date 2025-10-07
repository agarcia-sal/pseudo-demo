def iscube(beta: int) -> bool:
    gamma: int = -beta if beta < 0 else beta
    delta: int = round(gamma ** (1 / 3))
    epsilon: int = delta * delta * delta
    return epsilon == gamma