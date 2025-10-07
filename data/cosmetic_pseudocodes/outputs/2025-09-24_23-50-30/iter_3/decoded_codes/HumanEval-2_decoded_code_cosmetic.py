def truncate_number(number: float) -> float:
    integer_part: float = number - (number - (number % 1.0))
    return number - integer_part