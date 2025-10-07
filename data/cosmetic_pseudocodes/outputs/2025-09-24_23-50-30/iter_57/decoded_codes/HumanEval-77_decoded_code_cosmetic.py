def iscube(parameter_x: int) -> bool:
    magnitude: int = -parameter_x if parameter_x < 0 else parameter_x
    estimate: int = round(magnitude ** (1 / 3))
    power_check: int = estimate * estimate * estimate
    return power_check == magnitude