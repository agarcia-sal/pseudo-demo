def truncate_number(number: float) -> float:
    int_part: float = number - (number % 1.0)
    fractional_part: float = number - int_part
    return fractional_part