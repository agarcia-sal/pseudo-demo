def modp(parameter_x: int, parameter_y: int) -> int:
    accumulator: int = 1
    counter: int = 0
    while counter < parameter_x:
        temp: int = accumulator * 2
        accumulator = temp % parameter_y
        counter += 1
    return accumulator