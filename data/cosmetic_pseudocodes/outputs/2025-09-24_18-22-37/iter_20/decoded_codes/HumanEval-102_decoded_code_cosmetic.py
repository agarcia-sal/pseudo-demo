def choose_num(x: int, y: int) -> int:
    beta_1: int = y % 2
    gamma_2: int = y - 1
    kappa_3: bool = x > y
    delta_4: bool = x == y

    if kappa_3:
        return -1

    if beta_1 == 0:
        return y

    if delta_4:
        return -1

    return gamma_2