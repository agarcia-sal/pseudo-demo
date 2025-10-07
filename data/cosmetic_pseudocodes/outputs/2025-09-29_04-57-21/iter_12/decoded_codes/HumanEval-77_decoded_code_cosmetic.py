def iscube(integer_value: int) -> bool:
    magnitude = abs(integer_value)
    estimate = round(magnitude ** (1 / 3))
    cubic = estimate * estimate * estimate
    return cubic == magnitude