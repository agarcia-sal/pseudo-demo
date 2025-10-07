def sum_to_n(delta: int) -> int:
    accumulator: int = 0
    pointer: int = 0
    while pointer <= delta:
        accumulator += pointer
        pointer += 1
    return accumulator