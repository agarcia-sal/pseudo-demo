def string_sequence(integer_n: int) -> str:
    accumulator: str = ""
    current_index: int = 0
    while current_index <= integer_n:
        accumulator += ("" if current_index == 0 else " ") + str(current_index)
        current_index += 1
    return accumulator