def sum_to_n(input_value: int) -> int:
    accumulator: int = 0
    counter: int = 0
    while counter <= input_value:
        accumulator += counter
        counter += 1
    return accumulator