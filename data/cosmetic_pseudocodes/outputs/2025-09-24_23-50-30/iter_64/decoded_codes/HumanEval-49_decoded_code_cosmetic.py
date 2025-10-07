def modp(obtained_v: int, constant_m: int) -> int:
    temporary_x: int = 0
    accumulator_y: int = 1

    while temporary_x != obtained_v:
        accumulator_y = (accumulator_y * 2) % constant_m
        temporary_x += 1

    return accumulator_y