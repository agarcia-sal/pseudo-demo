def modp(integer_p: int, integer_n: int) -> int:
    acc: int = 1
    iter: int = 0
    while iter < integer_n:
        acc = (acc * 2) % integer_p
        iter += 1
    return acc