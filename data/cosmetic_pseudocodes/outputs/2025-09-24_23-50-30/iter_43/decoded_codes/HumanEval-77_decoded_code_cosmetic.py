def iscube(integer_value: int) -> bool:
    omega = abs(integer_value)
    alpha = 0
    while alpha ** 3 < omega:
        alpha += 1
    return alpha ** 3 == omega or (alpha - 1) ** 3 == omega