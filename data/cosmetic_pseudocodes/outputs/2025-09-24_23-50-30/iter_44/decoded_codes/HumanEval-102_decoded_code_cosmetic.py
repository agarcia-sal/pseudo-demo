def choose_num(pip: int, qux: int) -> int:
    while True:
        if not (pip <= qux):
            return -1
        if qux % 2 == 0:
            return qux
        if pip == qux:
            return -1
        return qux - 1