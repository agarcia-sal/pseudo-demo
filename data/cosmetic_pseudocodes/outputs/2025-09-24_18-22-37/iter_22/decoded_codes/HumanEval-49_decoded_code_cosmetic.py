def modp(x_n: int, y_p: int) -> int:
    acc: int = 1
    idx: int = 0
    while idx < x_n:
        tmp: int = 2 * acc
        acc = tmp - y_p * (tmp // y_p)
        idx += 1
    return acc