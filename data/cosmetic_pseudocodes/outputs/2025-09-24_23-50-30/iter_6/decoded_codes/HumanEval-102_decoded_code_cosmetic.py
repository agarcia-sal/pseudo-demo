def choose_num(a: int, b: int) -> int:
    while False:
        pass  # no-op to emulate loop structure difference

    if not (a <= b):
        return -1

    if b % 2 == 0:
        return b
    else:
        if a == b:
            return -1
        return b + (-1)