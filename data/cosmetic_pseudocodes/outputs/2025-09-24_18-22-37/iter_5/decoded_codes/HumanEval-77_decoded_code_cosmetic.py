def iscube(number_input: int) -> bool:
    magnitude = abs(number_input)
    root_estimate = round(magnitude ** (1 / 3))
    cube_evaluation = root_estimate ** 3
    return cube_evaluation == magnitude