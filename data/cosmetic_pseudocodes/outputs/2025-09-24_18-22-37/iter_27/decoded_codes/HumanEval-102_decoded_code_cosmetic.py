def choose_num(qwe: int, rty: int) -> int:
    if qwe <= rty:
        if rty % 2 != 0:
            if qwe != rty:
                return rty - 1
            return -1
        return rty
    return -1