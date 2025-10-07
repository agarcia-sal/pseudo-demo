def choose_num(x: int, y: int) -> int:
    # If x is greater than y, return -1
    if x > y:
        return -1

    # If y is even, return y
    if y % 2 == 0:
        return y

    # If x equals y, return -1
    if x == y:
        return -1

    # Otherwise, return y - 1
    return y - 1