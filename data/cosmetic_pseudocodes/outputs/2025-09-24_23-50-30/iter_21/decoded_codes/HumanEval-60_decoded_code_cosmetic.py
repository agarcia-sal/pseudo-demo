def sum_to_n(param_x: int) -> int:
    accumulator: int = 0
    counter: int = 0
    while counter <= param_x:
        accumulator += counter
        counter += 1
    return accumulator