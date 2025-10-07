def iscube(integer_value: int) -> bool:
    magnitude: int = integer_value
    if magnitude < 0:
        magnitude = -magnitude

    estimated_root: int = round(magnitude ** (1 / 3))
    reconstructed_cube: int = estimated_root ** 3

    return reconstructed_cube == magnitude