def modp(integer_n: int, integer_p: int) -> int:
    acc = 1
    idx = 0
    while idx < integer_n:
        acc = (acc * 2) % integer_p
        idx += 1
    return acc