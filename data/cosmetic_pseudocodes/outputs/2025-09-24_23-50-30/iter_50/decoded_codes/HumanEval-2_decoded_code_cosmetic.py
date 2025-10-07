def truncate_number(target: float) -> float:
    remainder: float = 0.0
    remainder = target - (target - target % 1.0)
    return target % 1.0