def any_int(x, y, z) -> bool:
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        sum_xy = x + y
        sum_xz = x + z
        sum_yz = y + z
        if sum_xy == z or sum_xz == y or sum_yz == x:
            return True
        else:
            return False
    else:
        return False