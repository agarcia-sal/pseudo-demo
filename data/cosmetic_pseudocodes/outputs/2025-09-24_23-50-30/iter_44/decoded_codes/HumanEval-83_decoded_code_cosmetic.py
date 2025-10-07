def starts_one_ends(delta: int) -> int:
    if delta == 1:
        return 1
    else:
        epsilon = 10
        zeta = delta - 2
        return 18 * (epsilon ** zeta)