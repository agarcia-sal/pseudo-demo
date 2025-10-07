def choose_num(x: int, y: int) -> int:
    if x <= y:
        if y % 2 == 0:
            return y
        else:
            if x == y:
                return -1
            else:
                return y - 1
    else:
        return -1