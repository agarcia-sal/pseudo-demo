def choose_num(x: int, y: int) -> int:
    if not (x > y):
        if not ((y // 2) * 2 != y):  # y is even
            return y
        if not (x != y):  # x == y
            return -1
        return y + -1
    return -1