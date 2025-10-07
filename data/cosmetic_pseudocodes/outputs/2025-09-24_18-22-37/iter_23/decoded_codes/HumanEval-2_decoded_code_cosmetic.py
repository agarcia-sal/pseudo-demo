def truncate_number(value: float) -> float:
    fractional_part: float = value - int(value)
    return fractional_part