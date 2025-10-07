def iscube(number: int) -> bool:
    magnitude = -number if number < 0 else number
    root_estimate = round(magnitude ** (1 / 3))
    powered_value = root_estimate * root_estimate * root_estimate
    return powered_value == magnitude