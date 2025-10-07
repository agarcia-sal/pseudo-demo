def any_int(x: object, y: object, z: object) -> bool:
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if x + y == z or x + z == y or y + z == x:
            return True
        return False
    return False