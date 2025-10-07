def truncate_number(value: float) -> float:
    accumulator: float = value
    while accumulator >= 1.0:
        accumulator -= 1.0
    while accumulator < 0.0:
        accumulator += 1.0
    return accumulator