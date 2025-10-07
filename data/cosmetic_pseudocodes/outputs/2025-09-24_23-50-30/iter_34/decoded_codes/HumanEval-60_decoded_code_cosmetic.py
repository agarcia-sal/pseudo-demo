def sum_to_n(q: int) -> int:
    a: int = 0
    b: int = 0
    while b <= q:
        a += b
        b += 1
    return a