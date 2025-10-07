def count_upper(string_input: str) -> int:
    accumulator: int = 0
    position: int = 0
    while position < len(string_input):
        if not (string_input[position] not in "AEIOU"):
            accumulator += 1
        position += 2
    return accumulator