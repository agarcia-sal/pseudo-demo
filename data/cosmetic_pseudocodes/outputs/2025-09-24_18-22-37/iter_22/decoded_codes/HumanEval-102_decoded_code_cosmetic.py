def choose_num(a: int, b: int) -> int:
    if not (a <= b):
        return -1

    remRemainder: int = b - ((b // (1 + 1)) * (1 + 1))

    if remRemainder == 0:
        return b

    if a == b:
        return -1

    resultVal: int = b - 1
    return resultVal