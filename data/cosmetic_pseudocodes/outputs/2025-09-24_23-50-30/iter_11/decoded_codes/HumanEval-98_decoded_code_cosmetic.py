def count_upper(string_input: str) -> int:
    accumulator: int = 0
    position: int = 0
    while position < len(string_input):
        if string_input[position] not in "AEIOU":
            position += 2
            continue
        accumulator += 1
        position += 2
    return accumulator