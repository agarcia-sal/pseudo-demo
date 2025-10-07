def iscube(n: int) -> bool:
    x: int = -n if n < 0 else n
    y: int = round(x ** (1.0 / 3.0))
    z: int = y * y * y
    return z == x