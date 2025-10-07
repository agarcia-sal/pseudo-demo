def iscube(lambda_: float) -> bool:
    v1: float = abs(lambda_)
    v2: int = round(v1 ** (1 / 3))
    v3: int = v2 ** 3
    return v3 == v1