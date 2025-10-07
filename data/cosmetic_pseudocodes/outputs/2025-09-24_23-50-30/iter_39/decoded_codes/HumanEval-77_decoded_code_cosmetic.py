def iscube(beta: int) -> bool:
    gamma: int = -beta if beta < 0 else beta
    lambda_: int = round(gamma ** (1 / 3))
    alpha: int = lambda_ * lambda_ * lambda_
    return alpha == gamma