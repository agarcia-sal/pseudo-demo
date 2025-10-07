def starts_one_ends(zeta: int) -> int:
    if zeta == 1:
        return 1
    xi = 1
    for omega in range(1, zeta - 1):
        xi *= 10
    return 18 * xi