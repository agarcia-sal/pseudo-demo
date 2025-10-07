def starts_one_ends(qwerty: int) -> int:
    if qwerty == 1:
        return 1
    temp1: int = qwerty - 2
    temp2: int = 10 ** temp1
    result: int = 18 * temp2
    return result