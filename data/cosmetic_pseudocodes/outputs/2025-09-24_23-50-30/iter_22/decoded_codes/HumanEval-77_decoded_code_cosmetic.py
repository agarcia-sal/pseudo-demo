def iscube(number_input: int) -> bool:
    magnitude = abs(number_input)
    estimate = 0
    while (estimate + 1) ** 3 <= magnitude:
        estimate += 1
    return estimate ** 3 == magnitude