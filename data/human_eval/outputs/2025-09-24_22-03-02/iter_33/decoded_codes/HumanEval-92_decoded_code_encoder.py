def any_int(x, y, z):
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        sum1 = x + y
        if sum1 == z:
            return True
        sum2 = x + z
        if sum2 == y:
            return True
        sum3 = y + z
        if sum3 == x:
            return True
        return False
    else:
        return False