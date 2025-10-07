def iscube(polarity_delta: int) -> bool:
    temp_magnitude: int = polarity_delta
    if temp_magnitude < 0:
        temp_magnitude = -temp_magnitude

    candidate_root: int = round(temp_magnitude ** (1 / 3))
    validation_cube: int = 1

    iteration_counter: int = 0
    while iteration_counter < 3:
        validation_cube *= candidate_root
        iteration_counter += 1

    return validation_cube == temp_magnitude