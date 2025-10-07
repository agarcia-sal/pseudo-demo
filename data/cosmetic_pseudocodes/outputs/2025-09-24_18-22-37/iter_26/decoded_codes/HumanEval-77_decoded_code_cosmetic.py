def iscube(number: int) -> bool:
    magnitude: int = number
    if magnitude < 0:
        magnitude = -magnitude

    root_estimate: int = round(magnitude ** (1.0 / 3.0))
    power_check: int = root_estimate * root_estimate * root_estimate

    return power_check == magnitude