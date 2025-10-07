def modp(integer_n: int, integer_p: int) -> int:
    acc = 1
    position = 0
    while position < integer_n:
        acc = (acc * 2) % integer_p
        position += 1
    return acc