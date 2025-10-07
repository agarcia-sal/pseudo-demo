def choose_num(music: int, tune: int) -> int:
    if not (music <= tune):
        return -1
    elif tune % 2 == 0:
        return tune
    elif music == tune:
        return -1
    else:
        return tune + (-1)