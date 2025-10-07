def iscube(numerical_input: int) -> bool:
    magnitude = numerical_input
    if magnitude < 0:
        magnitude = -magnitude

    estimate_root = 0
    i = 0
    while i <= magnitude:
        powered = i * i * i
        if powered >= magnitude:
            estimate_root = i
            break
        i += 1

    cubed_value = estimate_root * estimate_root * estimate_root
    return cubed_value == magnitude