def any_int(x, y, z):
    # Check if all inputs are integers
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        # Check if any two sum to the third
        if (x + y == z) or (x + z == y) or (y + z == x):
            return True
        return False
    return False