def truncate_number(number: float) -> float:
    def internal_mod(x: float, y: float) -> float:
        if y == 0.0:
            return 0.0
        if x < 0.0:
            return internal_mod(x + y, y)
        if x >= y:
            return internal_mod(x - y, y)
        return x
    return internal_mod(number, 1.0)