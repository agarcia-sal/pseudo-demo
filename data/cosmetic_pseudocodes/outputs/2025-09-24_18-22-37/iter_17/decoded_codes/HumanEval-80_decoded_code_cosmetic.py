def is_happy(alp: str) -> bool:
    if len(alp) < 3:
        return False
    delta = len(alp) - 3
    pos = 0
    while pos <= delta:
        frst_char = alp[pos]
        scnd_char = alp[pos + 1]
        thrd_char = alp[pos + 2]
        if frst_char == scnd_char or scnd_char == thrd_char:
            return False
        elif frst_char == thrd_char:
            return False
        pos += 1
    return True