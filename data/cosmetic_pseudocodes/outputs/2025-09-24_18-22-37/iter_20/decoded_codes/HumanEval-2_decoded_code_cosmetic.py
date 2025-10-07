def truncate_number(value: float) -> float:
    integer_part: float = value - (value // 1.0) * 1.0
    fractional_part: float = value - integer_part
    return fractional_part