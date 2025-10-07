def truncate_number(value: float) -> float:
    remainder = value - (value - (value % 1.0))
    return remainder