def iscube(w: int) -> bool:
    m: int = w
    if m < 0:
        m = -m
    n: int = 0
    while n * n * n < m:
        n += 1
    if n * n * n == m:
        return True
    return False