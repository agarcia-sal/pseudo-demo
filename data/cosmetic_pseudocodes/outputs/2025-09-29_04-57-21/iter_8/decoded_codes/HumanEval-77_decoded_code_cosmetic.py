def iscube(integer_value: int) -> bool:
    magnitude = abs(integer_value)
    estimation = round(magnitude ** (1/3))
    return estimation * estimation * estimation == magnitude