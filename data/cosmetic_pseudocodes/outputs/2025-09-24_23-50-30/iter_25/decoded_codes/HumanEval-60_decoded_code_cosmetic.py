def sum_to_n(count_target: int) -> int:
    accumulator: int = 0
    index: int = 0

    while not (index > count_target):
        accumulator += index
        index += 1

    return accumulator