def iscube(integer_value: int) -> bool:
    val_abs: int = integer_value
    if val_abs < 0:
        val_abs = -val_abs
    approx_root: int = round(val_abs ** (1 / 3))
    cubed: int = approx_root * approx_root * approx_root
    return cubed == val_abs