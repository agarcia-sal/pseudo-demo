def iscube(num: int) -> bool:
    val = abs(num)
    root_estimate = round(val ** (1 / 3))
    test_val = root_estimate * root_estimate * root_estimate
    return test_val == val