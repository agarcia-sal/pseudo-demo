def iscube(u: int) -> bool:
    v: int = -u if u < 0 else u
    w: int = round(v ** (1.0 / 3.0))
    x: int = w * w * w
    return x == v