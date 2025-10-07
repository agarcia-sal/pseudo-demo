def truncate_number(value: float) -> float:
    remainder: float = value - (value - (value % 1.0))
    return remainder