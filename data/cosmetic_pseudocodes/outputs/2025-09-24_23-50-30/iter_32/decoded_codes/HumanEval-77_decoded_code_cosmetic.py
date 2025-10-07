def iscube(integer_value: int) -> bool:
    alpha = abs(integer_value)
    beta = round(alpha ** (1 / 3))
    gamma = beta * beta * beta
    return gamma == alpha