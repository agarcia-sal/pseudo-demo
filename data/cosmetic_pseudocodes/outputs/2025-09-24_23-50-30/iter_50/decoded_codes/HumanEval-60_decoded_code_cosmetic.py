def sum_to_n(input_val: int) -> int:
    accumulator: int = 0
    counter: int = 0
    while counter <= input_val:
        accumulator += counter
        counter += 1
    return accumulator